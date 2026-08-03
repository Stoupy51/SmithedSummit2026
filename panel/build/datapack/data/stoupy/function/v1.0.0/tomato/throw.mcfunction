
#> stoupy:v1.0.0/tomato/throw
#
# @executed	as the player & at current position
#
# @within	stoupy:v1.0.0/tomato/on_use
#

# Let the freshly summoned tomato copy the item it was thrown with
tag @s add stoupy.tomato.thrower
execute anchored eyes positioned ^ ^ ^0.4 summon item_display run function stoupy:v1.0.0/tomato/init
tag @s remove stoupy.tomato.thrower

# Spend one tomato from the stack
item modify entity @s weapon.mainhand stoupy:v1.0.0/tomato/consume_one
playsound minecraft:entity.snowball.throw player @a[distance=..24] ~ ~ ~ 0.8 1.4

