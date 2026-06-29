#version 330
#moj_import <sdk:build/item.fsh/header.glsl>

#moj_import <minecraft:globals.glsl>

#moj_import <minecraft:fog.glsl>
#moj_import <minecraft:dynamictransforms.glsl>

uniform sampler2D Sampler0;

in float sphericalVertexDistance;
in float cylindricalVertexDistance;
in vec4 vertexColor;
in vec4 lightMapColor;
in vec4 overlayColor;
in vec2 texCoord0;

out vec4 fragColor;

flat in int sdk_id;
flat in int sdk_int;
flat in int sdk_int_b;
smooth in float sdk_float;
smooth in vec4 sdk_vec4;
smooth in vec4 sdk_vec4_b;
flat in ivec4 sdk_ivec4;
flat in mat4 sdk_mat4;
#moj_import <sdk:build/item.fsh/include.glsl>
void main() {
    vec4 color = texture(Sampler0, texCoord0);
#ifdef ALPHA_CUTOUT
    if (color.a < ALPHA_CUTOUT) {
        discard;
    }
#endif

    color *= vertexColor * ColorModulator;
    color.rgb = mix(overlayColor.rgb, color.rgb, overlayColor.a);
    color *= lightMapColor;

    fragColor = apply_fog(color, sphericalVertexDistance, cylindricalVertexDistance, FogEnvironmentalStart, FogEnvironmentalEnd, FogRenderDistanceStart, FogRenderDistanceEnd, FogColor);
    #moj_import <sdk:build/item.fsh/inject.glsl>
}
