
#> basic_template:v0.0.1/minute
#
# @within	basic_template:v0.0.1/tick
#

# Reset timer
scoreboard players set #minute basic_template.data 1

execute if score #spam basic_template.data matches 1 run say This is a message every minute

