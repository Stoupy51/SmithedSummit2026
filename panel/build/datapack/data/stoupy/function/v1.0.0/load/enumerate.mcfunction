
#> stoupy:v1.0.0/load/enumerate
#
# @within	#stoupy:enumerate
#

# If current major is too low, set it to the current major
execute unless score #stoupy.major load.status matches 1.. run scoreboard players set #stoupy.major load.status 1

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #stoupy.major load.status matches 1 unless score #stoupy.minor load.status matches 0.. run scoreboard players set #stoupy.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #stoupy.major load.status matches 1 if score #stoupy.minor load.status matches 0 unless score #stoupy.patch load.status matches 0.. run scoreboard players set #stoupy.patch load.status 0

