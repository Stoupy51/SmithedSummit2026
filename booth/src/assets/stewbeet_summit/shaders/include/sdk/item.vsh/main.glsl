// Forward the model-space vertex position to the fragment stage so it can raycast
// the procedural black hole. Replaces the legacy custom `c_` varying (the SDK does
// not allow adding inter-stage variables, so we reuse the provided `sdk_vec4`).
sdk_vec4 = vec4(Position, 1.0);
