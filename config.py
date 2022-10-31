from libqtile import hook
from settings.keys import mod, keys, lazy
from settings.path import qtile_path, path
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import screens, widget_defaults
from settings.mouse import mouse


import os
import subprocess



@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "urgent"
auto_minimize = True
wmname = "LG3D"