
#> basic_template:v0.0.1/load/main
#
# @within	basic_template:v0.0.1/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #basic_template.loaded load.status matches 1 run function basic_template:v0.0.1/load/secondary

