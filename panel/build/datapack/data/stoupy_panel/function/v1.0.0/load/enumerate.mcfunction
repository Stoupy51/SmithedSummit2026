
#> stoupy_panel:v1.0.0/load/enumerate
#
# @within	#stoupy_panel:enumerate
#

# If current major is too low, set it to the current major
execute unless score #stoupy_panel.major load.status matches 1.. run scoreboard players set #stoupy_panel.major load.status 1

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #stoupy_panel.major load.status matches 1 unless score #stoupy_panel.minor load.status matches 0.. run scoreboard players set #stoupy_panel.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #stoupy_panel.major load.status matches 1 if score #stoupy_panel.minor load.status matches 0 unless score #stoupy_panel.patch load.status matches 0.. run scoreboard players set #stoupy_panel.patch load.status 0

