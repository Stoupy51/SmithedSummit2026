#version 330
#moj_import <sdk:build/item.vsh/header.glsl>

#moj_import <minecraft:globals.glsl>

#moj_import <minecraft:light.glsl>
#moj_import <minecraft:fog.glsl>
#moj_import <minecraft:dynamictransforms.glsl>
#moj_import <minecraft:projection.glsl>
#moj_import <minecraft:sample_lightmap.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV1;
in ivec2 UV2;
in vec3 Normal;

uniform sampler2D Sampler1;
uniform sampler2D Sampler2;

out float sphericalVertexDistance;
out float cylindricalVertexDistance;
out vec4 vertexColor;
out vec4 lightMapColor;
out vec4 overlayColor;

out vec2 texCoord0;

flat out int sdk_id;
flat out int sdk_int;
flat out int sdk_int_b;
smooth out float sdk_float;
smooth out vec4 sdk_vec4;
smooth out vec4 sdk_vec4_b;
flat out ivec4 sdk_ivec4;
flat out mat4 sdk_mat4;
uniform sampler2D Sampler0;
#moj_import <sdk:build/item.vsh/include.glsl>
void main() {
    gl_Position = ProjMat * ModelViewMat * vec4(Position, 1.0);

    sphericalVertexDistance = fog_spherical_distance(Position);
    cylindricalVertexDistance = fog_cylindrical_distance(Position);

    vertexColor = minecraft_mix_light(Light0_Direction, Light1_Direction, Normal, Color);
    lightMapColor = sample_lightmap(Sampler2, UV2);
    overlayColor = texelFetch(Sampler1, UV1, 0);

    texCoord0 = UV0;
    #moj_import <sdk:build/item.vsh/inject.glsl>
}
