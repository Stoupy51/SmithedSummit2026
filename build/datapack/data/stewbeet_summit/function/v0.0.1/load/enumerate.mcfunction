
#> stewbeet_summit:v0.0.1/load/enumerate
#
# @within	#stewbeet_summit:enumerate
#

# If current major is too low, set it to the current major
execute unless score #stewbeet_summit.major load.status matches 0.. run scoreboard players set #stewbeet_summit.major load.status 0

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #stewbeet_summit.major load.status matches 0 unless score #stewbeet_summit.minor load.status matches 0.. run scoreboard players set #stewbeet_summit.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #stewbeet_summit.major load.status matches 0 if score #stewbeet_summit.minor load.status matches 0 unless score #stewbeet_summit.patch load.status matches 1.. run scoreboard players set #stewbeet_summit.patch load.status 1

