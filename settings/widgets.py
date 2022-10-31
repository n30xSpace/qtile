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
        fontsize=45,
        padding=-7
    )

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                
                widget.GroupBox(
                    highlight_method='line'
                    ),
                
                widget.Prompt(),
                
                widget.WindowName(
                    parse_text = 'None'
                    ),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                tri(fg='color1', bg='black'),
                widget.Net(
                    **base(bg='color1'),
                    format = '{down} ↓↑ {up}'
                ),
                tri(fg='color2', bg='color1'),
                widget.Memory(
                    **base(bg='color2'),
                  measure_mem='G' 
                ),
                tri(fg='color3', bg='color2'),             
                widget.CPU(
                    **base(bg='color3'),
                  type='line', line_width=1 
                ),
                tri(fg='color4', bg='color3'),
                widget.Clock(
                    **base(bg='color4'),
                    format="%I:%M %p"
                    ),
                tri(fg='color5', bg='color4'),
                widget.QuickExit(
                    **base(bg='color5'),
                    default_text='', 
                    countdown_format='{}',
                    ),
                    
                
            ],
            24,
        ),
    ),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()