from libqtile.config import Key, Group, Match
from settings.keys import mod, keys, lazy

__groups = {
    1: Group("", matches=[Match(wm_class=["firefox"])]),
    2: Group("", matches=[Match(wm_class=["Code"])]),
    3: Group("", matches=[Match(wm_class=["Spotify"])]),
    4: Group("", matches=[Match(wm_class=["kitty"])]),
    5: Group("MIX", matches=[Match(wm_class=[])]),
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])