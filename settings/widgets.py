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
        text="", # Icon: nf-oct-triangle_left
        fontsize=58,
        padding=-9
    )

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.QuickExit(
                    **base(bg='color5'),
                    default_text='X',
                    countdown_format='{}',
                    
                    ), 
                widget.Spacer(),
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method='line'
                    ),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                tri(fg='color6', bg='black'),
                widget.PulseVolume(
                    **base(bg='color6'),
                ),
                tri(fg='color1', bg='color6'),
                widget.Net(
                    **base(bg='color1'),
                    format = '{down} ↓↑ {up}',
                    prefix='M',
                ),
                tri(fg='color2', bg='color1'),
                widget.Memory(
                    **base(bg='color2'),
                    format='{MemUsed: .0f}{mm}',
                ),
                tri(fg='color3', bg='color2'),             
                widget.CPU(
                    **base(bg='color3'),
                    format='{load_percent}%' 
                ),
                tri(fg='color4', bg='color3'),
                widget.Clock(
                    **base(bg='color4'),
                    format='%d/%m-%H:%M'
                    ),                                                 
            ],
            30,
            opacity=0.92,
        ),
    ),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()