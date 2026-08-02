
#> stoupy_panel:reef/register/page/panel
#
# @within	stoupy_panel:reef/register_namespace
#

data modify storage stoupy_panel:reef register.mini."stoupy_panel:panel" set value {"page_count": 6, "model": "stoupy_panel:reef/mini/panel"}
function reef:api/register/mini {identifier: "stoupy_panel:panel", storage_path: 'stoupy_panel:reef register.mini."stoupy_panel:panel"'}

