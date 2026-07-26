
#> stewbeet_summit:entities/kill
#
# @within	#summit.booth:stewbeet_summit/entities/kill
#

execute as @e[type=mannequin,tag=stewbeet_summit.entity] run data merge entity @s {DeathTime: 19s}
kill @e[tag=stewbeet_summit.entity]

