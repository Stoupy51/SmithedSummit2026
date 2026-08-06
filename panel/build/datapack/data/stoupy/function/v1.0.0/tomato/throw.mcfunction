
#> stoupy:v1.0.0/tomato/throw
#
# @executed	as the player & at current position
#
# @within	stoupy:v1.0.0/tomato/on_use
#

# Let the freshly summoned tomato copy the item it was thrown with
execute anchored eyes positioned ^ ^ ^0.4 summon item_display run function stoupy:v1.0.0/tomato/init

# Spend one tomato from the stack
item modify entity @s weapon.mainhand stoupy:v1.0.0/tomato/consume_one
playsound minecraft:entity.snowball.throw player @s ~ ~ ~ 0.25 1.4

