
#> stewbeet_summit:entities/kill
#
# @within	#summit.booth:stewbeet_summit/entities/kill
#			stewbeet_summit:entities/summon
#

execute as @e[type=mannequin,tag=summit.booth_entity.stewbeet_summit] run data merge entity @s {DeathTime: 19s}
kill @e[tag=summit.booth_entity.stewbeet_summit]

