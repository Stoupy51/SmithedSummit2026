// Black hole accretion-disk effect for the Smithed Summit 2026 background.
// All helpers are namespaced (stewbeet_summit_*) per the SDK convention.
// Constants are kept as function-local consts to avoid bloating the global scope.

// Volumetric ray-marching of the accretion disk.
vec4 stewbeet_summit_computeAccretionDisk(vec3 localPos, float animTime) {
    const float marchSteps = 20.0;
    const float fbmOctaves = 5.0;

    vec4 accumulatedColor = vec4(0.0);
    vec3 normalizedPos = normalize(localPos);
    float rayDist = animTime; // loop accumulator, do not rename
    for (float stepDist = 0.0, stepSize = 0.0, iterCount = 0.0; iterCount < marchSteps; iterCount++) {
        vec3 samplePos = stepDist * normalizedPos;
        // Cylindrical coordinates to spiral around the axis
        samplePos = vec3(
            atan(samplePos.y / 0.2, samplePos.x) * 2.0,
            samplePos.z / 3.0,
            length(samplePos.xy) - 5.0 - stepDist * 0.2
        );
        // Fractal noise (FBM)
        for (stepSize = 1.0; stepSize < fbmOctaves; stepSize++) {
            samplePos += sin(samplePos.yzx * stepSize + rayDist + 0.3 * iterCount) / stepSize;
        }
        stepDist += stepSize = length(vec4(0.4 * cos(samplePos) - 0.4, samplePos.z));
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

    // Ray / infinite cylinder intersection (accretion disk)
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
    vec4 diskColor = stewbeet_summit_computeAccretionDisk(localHitPos, GameTime * 320.0);

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
