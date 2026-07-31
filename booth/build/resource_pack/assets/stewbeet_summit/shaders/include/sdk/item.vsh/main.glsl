// Forward what the fragment stage needs to raycast the procedural black hole. The SDK
// does not allow adding inter-stage variables, so we reuse the provided `sdk_vec4` and
// `sdk_vec4_b` (this replaces the legacy custom `a_` / `c_` varyings).
//
// `sdk_vec4` is the world-space fragment position and `sdk_vec4_b` the same pixel
// projected onto the camera near plane; their difference is the view ray. The eye stops
// being at the origin as soon as view bobbing is applied, so `normalize(Position)` alone
// is wrong. `sdk_vec4_b` stays a vec4 because the perspective divide has to happen after
// interpolation to stay linear.
sdk_vec4   = vec4(Position, 1.0);
sdk_vec4_b = inverse(ProjMat * ModelViewMat) * gl_Position.xyww;
