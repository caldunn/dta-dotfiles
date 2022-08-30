# -*- encoding: utf-8 -*-
import os
import re
import socket
import subprocess

import libqtile.core.manager
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

from libqtile.log_utils import logger
mod = "mod4"  # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"  # My terminal of choice
myBrowser = "brave"  # My terminal of choice


def abc(qtile: libqtile.core.manager.Qtile, *args):
    """
    This assumes that there are only 2 screens. Because that's what I have :)
    """
    to_screen = 0 if qtile.current_window.group.screen.index == 1 else 1
    qtile.current_window.togroup(qtile.screens[to_screen].group.name)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


keys = [
    ### The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key(["mod1"], "space",
        lazy.spawn("dmenu_run -p 'Run: ' -fn 'JetBrains Mono-12' -g 3 -l 5"),
        desc='Run Launcher'
        ),
    Key([mod], "w",
        lazy.spawn(myBrowser),
        desc='Qutebrowser'
        ),
    Key([mod, "shift"], "s",
        lazy.spawn("flameshot gui"),
        desc='Take a screenshot'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod, "shift"], "q",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "F2",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    Key([mod, "shift"], "F3",
        lazy.spawn('/home/caleb/.local/share/JetBrains/Toolbox/bin/jetbrains-toolbox --minimize'),
        desc='Shutdown Qtile'
        ),
    # Switch focus to specific monitor (out of three)
    Key([mod], "b",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        desc='Move down a section in treetab'
        ),
    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    Key([mod, "control"], "semicolon",
        lazy.spawn("systemctl suspend"),
        desc='Sleeptime...'
        ),
    Key([mod, "shift"], "period",
        lazy.function(abc),
        desc='Custom Func...'
        ),
    Key([mod, "control"], "period",
        lazy.function(switch_screens),
        desc='Switch the screens'
        ),
]




groups = [Group("WWW", {'layout': 'monadtall'}),
          Group("DEV", {'layout': 'monadtall'}),
          Group("SYS", {'layout': 'monadtall'}),
          Group("DOC", {'layout': 'monadtall'}),
          Group("VBOX", {'layout': 'monadtall'}),
          Group("CHAT", {'layout': 'monadtall'}),
          Group("MUS", {'layout': 'monadtall'}),
          Group("VID", {'layout': 'monadtall'}),
          Group("GFX", {'layout': 'floating'})]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder

dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "#be5046",
                "border_normal": "1D2330"
                }

layouts = [
        # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Zoomy(**layout_theme),
    # layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font="Ubuntu",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color="1c1f24",
        active_bg="c678dd",
        active_fg="000000",
        inactive_bg="a9a1e1",
        inactive_fg="1c1f24",
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme)
]

""" colors = [["#282c34", "#282c34"],  # panel background
          ["#3d3f4b", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#74438f", "#74438f"],  # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
          ["#e1acff", "#e1acff"],  # window name
          ["#ecbbfb", "#ecbbfb"]]  # backbround for inactive screens """

colors = [["#282c34", "#282c34"],  # panel background
          ["#3d3f4b", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#e06c75", "#e06c75"],  # border line color for current tab
          ["#282c34", "#282c34"],  # border line color for 'other tabs' and color for 'odd widgets'
          ["#282c34", "#282c34"],  # color for the 'even widgets'
          ["#e06c75", "#e06c75"],  # window name
          ["#4b5263", "#4b5263"]]  # backbround for inactive screens

light_grey = ["#ABB2BF", "#ABB2BF"]
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=12,
    padding=15,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font="JetBrains Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=light_grey, #colors[4],
            other_current_screen_border=colors[6],
            # other_screen_border=colors[4],
            other_screen_border=light_grey,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowCount(
            fontsize=14,
            foreground=colors[6],
            background=colors[0],
            ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.WindowName(
            fontsize=14,
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),

        widget.Net(
            interface="enp6s0",
            format='{down} ↓ {up} ↑',
            foreground=colors[2],
            background=colors[5],
        ),

        widget.CPU(
            foreground=colors[2],
            background=colors[4],
            format="{freq_current}GHz {load_percent}%"
        ),

        widget.ThermalSensor(
            tag_sensor='Package id 0',
            fmt="C 🌡{}",
            foreground=colors[2],
            background=colors[4],
            threshold=90,
        ),
        widget.ThermalSensor(
            tag_sensor='junction',
            fmt="G 🌡{}",
            foreground=colors[2],
            background=colors[4],
            threshold=90,
        ),
        widget.CheckUpdates(
            update_interval=600,
            distro="Arch_checkupdates",
            display_format="{updates} Updates",
            no_update_string="No Updates",
            foreground=colors[2],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
            background=colors[5]
        ),
        widget.Memory(
            format="💾{MemUsed: .0f} /{MemTotal: .0f}",
            foreground=colors[2],
            background=colors[4],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e btop')},
        ),
        widget.PulseVolume(
            volume_app="pamixer",
            foreground=colors[2],
            background=colors[5],
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
        ),

        widget.Clock(
            foreground=colors[2],
            background=colors[5],
            format="%a, %d %B - %H:%M"
        ),
        widget.Systray(
            padding=0,
            background=colors[0],
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widget_screen_1 = init_widgets_list()
    del widget_screen_1[-1:]  # Slicing removes unwanted widgets (systray)
    return widget_screen_1


def init_widgets_screen2():
    widgets_screen_2 = init_widgets_list()
    return widgets_screen_2  # Monitor 2 will display all widgets in widgets_list


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),  # tastyworks exit box
    Match(title='Qalculate!'),  # qalculate-gtk
    Match(wm_class='kdenlzive'),  # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    # subprocess.call([f'{home}/.local/share/JetBrains/Toolbox/bin/jetbrains-toolbox', '--minimize'])
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
