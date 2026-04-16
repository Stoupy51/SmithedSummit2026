
#> basic_template:v0.0.1/tick_2
#
# @within	basic_template:v0.0.1/tick
#

# Reset timer
scoreboard players set #tick_2 basic_template.data 1

execute if score #spam basic_template.data matches 1 run say This is a SPAM message every 2 ticks

