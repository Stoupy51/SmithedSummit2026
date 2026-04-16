
#> basic_template:v0.0.1/tick
#
# @within	basic_template:v0.0.1/load/tick_verification
#

# Timers
scoreboard players add #tick_2 basic_template.data 1
scoreboard players add #second_5 basic_template.data 1
scoreboard players add #minute basic_template.data 1
execute if score #tick_2 basic_template.data matches 3.. run function basic_template:v0.0.1/tick_2
execute if score #second_5 basic_template.data matches 90.. run function basic_template:v0.0.1/second_5
execute if score #minute basic_template.data matches 1200.. run function basic_template:v0.0.1/minute

