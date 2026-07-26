// Black hole accretion-disk effect for the Smithed Summit 2026 background.
// All helpers are namespaced (stewbeet_summit_*) per the SDK convention.
// Constants are kept as function-local consts to avoid bloating the global scope.

// Ray-march budget for the accretion disk.
//
// The disk is drawn on a ~16x10 block backdrop, so it can cover most of the
// screen: its cost scales with the framebuffer, not with the model. Spending a
// fixed *step* budget therefore makes the shader several times more expensive at
// 1440p/4K than at 1080p. Spend a roughly fixed *pixel* budget instead and let
// the step count shrink as the framebuffer grows. ScreenSize is a uniform, so
// every fragment of the draw takes the same branch.
int stewbeet_summit_marchSteps() {
    const float baseSteps  = 20.0;               // steps at the reference resolution
    const float minSteps   = 8.0;                // floor: below this the disk visibly bands
    const vec2  baseScreen = vec2(1920.0, 1080.0);

    float pixelRatio = (ScreenSize.x * ScreenSize.y) / (baseScreen.x * baseScreen.y);
    // sqrt() so 4K (4x the pixels) halves the step count instead of quartering it:
    // 1080p -> 20 steps, 1440p -> 15, 4K -> 10.
    float budget = baseSteps / max(sqrt(pixelRatio), 1.0);
    return int(max(budget, minSteps));
}

// Volumetric ray-marching of the accretion disk.
//
// Note: a saturation-based early-out is tempting here (the accumulator only ever
// grows, so tanh() could be clamped early) but it is not worth the per-step test:
// the accumulator averages ~8 and reaches the ~40 needed to pin tanh() on well
// under 1% of rays. The step budget below is the lever that actually pays.
vec4 stewbeet_summit_computeAccretionDisk(vec3 localPos, float animTime, int marchSteps) {
    const int   fbmOctaves = 4;
    const float minStepLen = 1e-4;   // keeps a degenerate step from dividing by zero

    vec4 accumulatedColor = vec4(0.0);
    vec3 normalizedPos = normalize(localPos);
    float stepDist = 0.0;

    for (int iter = 0; iter < marchSteps; iter++) {
        float iterCount = float(iter);
        vec3 samplePos = stepDist * normalizedPos;
        // Cylindrical coordinates to spiral around the axis
        samplePos = vec3(
            atan(samplePos.y / 0.2, samplePos.x) * 2.0,
            samplePos.z / 3.0,
            length(samplePos.xy) - 5.0 - stepDist * 0.2
        );
        // Fractal noise (FBM). Constant bounds so the compiler unrolls it and folds
        // the 1/octave reciprocals.
        float phase = animTime + 0.3 * iterCount;
        for (int octave = 1; octave <= fbmOctaves; octave++) {
            float scale = float(octave);
            samplePos += sin(samplePos.yzx * scale + phase) / scale;
        }
        float stepSize = max(length(vec4(0.4 * cos(samplePos) - 0.4, samplePos.z)), minStepLen);
        stepDist += stepSize;
        accumulatedColor += (cos(samplePos.x + iterCount * 0.4 + stepDist + vec4(6.0, 1.0, 2.0, 0.0)) + 1.0) / stepSize;
    }
    accumulatedColor = tanh(accumulatedColor * accumulatedColor / 4e2);
    return accumulatedColor;
}

// Full black hole render (raycasting + visual effects).
// `rayDir` is the model-space vertex position forwarded from the vertex stage.
vec4 stewbeet_summit_computeBlackHole(vec3 rayDir) {
    const vec3  blackHoleAxis   = vec3(0.0, -0.4, -0.9); // black hole rotation axis
    const float diskRadius      = 0.4;                   // accretion disk radius
    const float timeScale       = 0.5;                   // animation speed
    const float effectIntensity = 1.0;                   // overall effect intensity
    const vec3  rimColor        = vec3(0.64, 0.0, 0.0);  // rim color (red)
    const vec3  coreGlowColor   = vec3(0.04, 0.3, 0.47); // core glow color (blue-green)

    vec3 viewDir = normalize(rayDir);
    viewDir = vec3(-viewDir.x, viewDir.y, -viewDir.z); // 180 deg yaw rotation
    vec3 diskCenter = blackHoleAxis * (GameTime * timeScale);
    vec3 axisRef    = diskCenter;

    // Ray / infinite cylinder intersection (accretion disk).
    //
    // These two discards read like a fast path for rays that miss the disk, but they
    // are not one: the cylinder is infinite and diskCenter never gets further than
    // ~0.49 from the origin, so in practice every fragment of the backdrop hits it
    // and goes on to march. Treat the march cost below as paid by *every* pixel the
    // black hole covers, not just the bright ones.
    float axisDotView  = dot(blackHoleAxis, viewDir);
    float axisDotRef   = dot(blackHoleAxis, axisRef);
    float cylA         = 1.0 - axisDotView * axisDotView;
    float cylB         = 2.0 * (dot(viewDir, axisRef) - axisDotView * axisDotRef);
    float cylC         = dot(axisRef, axisRef) - axisDotRef * axisDotRef - diskRadius * diskRadius;
    float discriminant = cylB * cylB - 4.0 * cylA * cylC;
    if (discriminant < 0.0) discard;

    float sqrtDisc = sqrt(discriminant);
    float invDenom = 1.0 / (2.0 * cylA);
    float t0       = (-cylB - sqrtDisc) * invDenom;
    float t1       = (-cylB + sqrtDisc) * invDenom;

    float hitDist = -1.0;
    if      (t0 > 0.0 && t1 > 0.0) hitDist = min(t0, t1);
    else if (t0 > 0.0)             hitDist = t0;
    else if (t1 > 0.0)             hitDist = t1;
    if (hitDist < 0.0) discard;

    // Hit point and local disk basis
    vec3 hitPoint      = diskCenter + viewDir * hitDist;
    vec3 axisDir       = blackHoleAxis;
    vec3 tangentHelper = abs(axisDir.y) < 0.9 ? vec3(0.0, 1.0, 0.0) : vec3(1.0, 0.0, 0.0);
    vec3 tangentU      = normalize(cross(axisDir, tangentHelper));
    vec3 tangentV      = cross(axisDir, tangentU);
    vec3 localHitPos   = vec3(dot(hitPoint, tangentU), dot(hitPoint, tangentV), dot(hitPoint, axisDir));

    // Disk color via ray-marching
    vec4 diskColor = stewbeet_summit_computeAccretionDisk(localHitPos, GameTime * 320.0, stewbeet_summit_marchSteps());

    // Fresnel effect (bright rim)
    vec3 axialProjection = blackHoleAxis * dot(hitPoint, blackHoleAxis);
    vec3 surfaceNormal   = normalize(hitPoint - axialProjection);
    float fresnel        = 1.0 - max(0.0, dot(surfaceNormal, -viewDir));
    float fresnelPow2    = fresnel * fresnel;
    float fresnelPow4    = fresnelPow2 * fresnelPow2;
    vec3 rimGlow         = coreGlowColor * fresnelPow4 * effectIntensity;

    // Axial glow (along black hole axis)
    float axialDist = dot(hitPoint, blackHoleAxis);
    float axialGlow = exp(-axialDist * axialDist * 0.1);
    vec3 axialColor = rimColor * axialGlow * effectIntensity;

    // Additive composition (screen blend)
    vec3 invDiskColor = vec3(1.0) - diskColor.rgb;
    diskColor.rgb = vec3(1.0) - invDiskColor * (vec3(1.0) - rimGlow) * (vec3(1.0) - axialColor);

    // Edge fade
    float edgeFade = smoothstep(-1.0, 1.0, axialDist);
    diskColor.a *= edgeFade;

    // Black background + final composite
    vec4 finalColor = mix(vec4(0.0, 0.0, 0.0, 1.0), diskColor, diskColor.a);
    finalColor.a = 1.0;
    return finalColor;
}
