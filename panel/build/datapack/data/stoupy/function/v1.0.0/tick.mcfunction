
#> stoupy:v1.0.0/tick
#
# @within	stoupy:v1.0.0/load/tick_verification
#

tag @a[advancements={stoupy:tomato/use=false},tag=stoupy.tomato.used] remove stoupy.tomato.used
advancement revoke @a only stoupy:tomato/use

execute as @e[type=item_display, tag=stoupy.tomato] at @s run function stoupy:v1.0.0/tomato/tick

