import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=1)

green_text = {'color':'green'}

def layout():
    return html.Div([dcc.Markdown('### Academic Experience', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2018 - May 2019*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Teaching assistant** \n'
                         '  *Environmental Fluid Mechanics* - Professor [J. Plazas](https://www.linkedin.com/in/jplazas)\n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         link_target='_blank',
                         className='ms-3'),
            html.Ul([
                html.Li('Create deliverable workshops and grade them.'),
                html.Li('Assist students during question hours.'),
                html.Li('Assist during field work')
            ])
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2021 - Dec. 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Teaching assistant** \n'
                         '  *Geophysics* - Professor [I. Molina](https://www.linkedin.com/in/indira-molina-77123b40)\n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         link_target='_blank',
                         className='ms-3'),
            html.Ul([
                html.Li('Create deliverable workshops and grade them.'),
                html.Li('Assist students during question hours.'),
            ])
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Professional Experience', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2021 - Nov. 2021*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Technical advisor on Agrosat services** \n'
                         '  **Nutrición de plantas S.A.** - Tuluá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
            html.Ul([
                html.Li('Responsible of the making of "Pilot study of Heavy Metal contamination in Avocado crops (Var. Hass)'
                        'and feasibility analysis of Crosscheck methodology in Heavy Metal distribution"'),
                html.Li('Support in the implementation of soil diagnostic services for agriculture (Nutricheck)'),
            ])
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Nov. 2021 - Jan. 2022*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Independent Professional on research project** \n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
            dcc.Markdown('- Conducting and writing the paper of the study "Residential radon concentrations in Bogota and'
                         'neighbouring municipalities, Colombia: Results of an exploratory study" under the supervision' 
                         'of professor [C. Huguet](https://www.linkedin.com/in/carme-huguet-7769b991/)',
                         link_target='_blank')
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*May 2022 - Jul. 2022*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**GIS technology advisor** \n'
                         '  **Avinal S. A.** - Medellín, Antioquia',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
            dcc.Markdown('- Theorical and practical consulting in Geo-Information Systems (QGIS) for helping in the building'
                         'of an Environmental Master Plan for *Granja Aurora* a farm part of Avinal S.A.'
                        )
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'})])