// The SDK has already gated this surface by its namespace id, so we can render
// the black hole directly. The model-space position arrives via `sdk_vec4` (set
// in the vertex stage) and is used as the ray direction.
fragColor = stewbeet_summit_computeBlackHole(sdk_vec4.xyz);
