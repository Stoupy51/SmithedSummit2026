
#> stewbeet_summit:entities/summon
#
# @within	#summit.booth:stewbeet_summit/entities/summon
#

# Clear any previous booth entities so repeated calls never stack
function stewbeet_summit:entities/kill

# Entrance decorations + presentation walls (reset back on page 0)
scoreboard objectives add stewbeet_summit.page dummy
function stewbeet_summit:intro/setup
function stewbeet_summit:walls/setup
function stewbeet_summit:walls/reset

