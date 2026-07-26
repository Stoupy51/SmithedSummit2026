#version 330
ivec2 sdk_atlasSize = textureSize(Sampler0, 0);
ivec2 sdk_iuv = ivec2(UV0 * sdk_atlasSize);
if (ivec4(texelFetch(Sampler0, sdk_iuv, 0) * 255.0) != ivec4(1, 2, 3, 255)) {sdk_id = 0; return;};
ivec4 sdk_col = ivec4(texelFetch(Sampler0, sdk_iuv + ivec2(1, 0), 0) * 255.0);
sdk_id = (sdk_col.r << 24) | (sdk_col.g << 16) | (sdk_col.b << 8) | sdk_col.a;
sdk_B_stewbeet_summit(sdk_iuv, sdk_atlasSize);