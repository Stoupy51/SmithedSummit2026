
#> basic_template:v0.0.1/load/confirm_load
#
# @within	basic_template:v0.0.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"translate":"basic_template.loaded_basic_template_v0_0_1","color":"green"}
scoreboard players set #basic_template.loaded load.status 1
function basic_template:v0.0.1/load/set_items_storage

# Add a message when loading
say Here is a message when loading the datapack, located in `src/link.py`

