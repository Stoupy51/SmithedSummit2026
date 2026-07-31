// The SDK has already gated this surface by its namespace id, so we can render the black
// hole directly. `sdk_vec4` carries the world-space fragment position and `sdk_vec4_b`
// the matching near-plane position, both set in the vertex stage.
fragColor = stewbeet_summit_computeBlackHole(sdk_vec4.xyz, sdk_vec4_b);
