
#> stoupy_panel:v1.0.0/tick
#
# @within	stoupy_panel:v1.0.0/load/tick_verification
#

tag @a[advancements={stoupy_panel:tomato/use=false},tag=stoupy_panel.tomato.used] remove stoupy_panel.tomato.used
advancement revoke @a only stoupy_panel:tomato/use

execute as @e[type=item_display, tag=stoupy_panel.tomato] at @s run function stoupy_panel:v1.0.0/tomato/tick

