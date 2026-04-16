
#> basic_template:v0.0.1/load/enumerate
#
# @within	#basic_template:enumerate
#

# If current major is too low, set it to the current major
execute unless score #basic_template.major load.status matches 0.. run scoreboard players set #basic_template.major load.status 0

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #basic_template.major load.status matches 0 unless score #basic_template.minor load.status matches 0.. run scoreboard players set #basic_template.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #basic_template.major load.status matches 0 if score #basic_template.minor load.status matches 0 unless score #basic_template.patch load.status matches 1.. run scoreboard players set #basic_template.patch load.status 1

