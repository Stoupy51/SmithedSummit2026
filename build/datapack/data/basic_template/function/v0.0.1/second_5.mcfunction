
#> basic_template:v0.0.1/second_5
#
# @within	basic_template:v0.0.1/tick
#

# Reset timer
scoreboard players set #second_5 basic_template.data -10

execute if score #spam basic_template.data matches 1 run say This is a SPAM message every 5 seconds

