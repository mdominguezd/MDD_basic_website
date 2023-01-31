import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Martín Domínguez Durán', className='mt-3'),
    dcc.Markdown('### Personal info', style={'color':'gray'}),
    dcc.Markdown('**Phone Number**', style=green_text),
    dcc.Markdown('+31 0651120353'),
    dcc.Markdown('**Email**', style=green_text),
    dcc.Markdown('martin.dominguez.duran@gmail.com'),
    dcc.Markdown('**Linkedin**', style=green_text),
    dcc.Markdown('[www.linkedin.com](https://www.linkedin.com/in/mart%C3%ADn-dom%C3%ADnguez-dur%C3%A1n-54b4681b6/)', link_target='_blank'),
    dcc.Markdown('**GitHub**', style=green_text),
    dcc.Markdown('[www.github.com](https://github.com/mdominguezd)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')