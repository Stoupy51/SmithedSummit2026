
#> stewbeet_summit:booth/on_enter
#
# @within	???
#

advancement grant @s only summit.sticker_book:stewbeet_summit/stewbeet

# Alone in the booth (the summit tags players inside with summit.in_booth.<ns>):
# reset every presentation wall to page 0 for a fresh visit
execute store result score #in_booth stewbeet_summit.data if entity @a[tag=summit.in_booth.stewbeet_summit]
execute if score #in_booth stewbeet_summit.data matches ..1 run function stewbeet_summit:walls/reset

