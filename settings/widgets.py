from libqtile import bar, widget
from libqtile.config import Screen
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }
    
def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def tri(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=47,
        padding=-7
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line'
                    ),
                widget.WindowName(
                    empty_group_string='',
                    ),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                widget.Sep(
                    **base(fg='dark'), 
                    ),
                widget.PulseVolume(
                    **base(bg='color6'),   
                ),
                widget.Sep(
                    **base(fg='dark'), 
                    ),
                widget.Net(
                    interface='enp5s0',
                    format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                    **base(bg='color1'),
                    prefix='M',
                ),
                widget.Sep(
                    **base(fg='dark'), 
                    ),
                widget.MemoryGraph(
                    **base(bg='color2'),
                    format='{MemUsed: .0f}{mm}',
                ),
                widget.Sep(
                    **base(fg='dark'), 
                    ),            
                widget.CPUGraph(
                    **base(bg='color3'),
                    format='{load_percent}%' 
                ),
                widget.Sep(
                    **base(fg='dark'), 
                    ),
                widget.Clock(
                    **base(bg='color4'),
                    format='%d-%m[%H:%M]'
                    ),                                                 
            ],
            24,
            opacity=0.8,
        ),
    ),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()