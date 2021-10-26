local awful = require("awful")
local utils = require("utils")

terminal = "kitty"
browser1 = "brave"
browser2 = "firefox"
editor = "code"
editor_cmd = terminal .. editor
file1 = terminal .. " -e " .. "ranger"
file2 = "pcmanfm"
music = terminal .. " -e ncmpcpp"

thermal_zone = 1

lockscreen = "betterlockscreen -l dimblur"

awful.layout.layouts = {
    awful.layout.suit.tile,
    awful.layout.suit.tile.left,
    awful.layout.suit.tile.bottom,
    awful.layout.suit.corner.nw,
    utils.centerwork,
    awful.layout.suit.floating,
}

awful.util.tagnames = {
	{
		{name = "1", sel = true},
		{name = "2", sgap = true},
		{name = "3", lay = awful.layout.layouts[3], mw = 0.87},
		{name = "4"},
		{name = "5"},
		{name = "6"},
		{name = "7"},
		{name = "8"},
		{name = "9"},
		{name = "10"},
	},
	{
		{name = "1", sel = true},
		{name = "2"},
		{name = "3"},
		{name = "4"},
		{name = "5"},
		{name = "6"},
		{name = "7"},
		{name = "8"},
		{name = "9"},
		{name = "10"},
	}
}
