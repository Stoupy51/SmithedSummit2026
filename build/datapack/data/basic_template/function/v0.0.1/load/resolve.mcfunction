
#> basic_template:v0.0.1/load/resolve
#
# @within	#basic_template:resolve
#

# If correct version, load the datapack
execute if score #basic_template.major load.status matches 0 if score #basic_template.minor load.status matches 0 if score #basic_template.patch load.status matches 1 run function basic_template:v0.0.1/load/main

