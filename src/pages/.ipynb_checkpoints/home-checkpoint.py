import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    html.Div([],style = {'height':50}),
    dcc.Markdown('# Martín Domínguez Durán', style={'textAlign':'center'}),
    dcc.Markdown('**Wageningen, Netherlands**', style={'textAlign': 'center'}),
    html.Div([html.Img(src='../assets/FOTO_MDD_1.jpg', style = {'height' : 100, 'width' : 100})],
             style = {'textAlign' : 'center'}
            ),
    
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('Environmental Engineer and Geoscientist from *Los Andes University, Bogotá, Colombia* and MSc Geo-Information student at\n'
                 '*Wageningen University & Research, The Netherlands*. I am a **dynamic**, **hardworking** and **curious** professional with a particular\n'
                 'interest in research topics involving environmental health, environmental modeling, data science, Geographic Information Systems\n'
                 'and remote sensing.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),
    
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2016 - Dec. 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('B.Sc. Environmental Engineer (GPA: 4.45/5) - *Cum Laude*\n'
                         '**Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jan. 2018 - Dec. 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('B.Sc. Geoscientist (GPA: 4.45/5) \n'
                         '**Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2017 - May 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Minor in Photography \n'
                         '**Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Aug. 2022 - present*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('M.Sc. Geo-Information Science \n'
                         '**Wageningen University & Research** - Wageningen, Netherlands',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Academic Experience', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2018 - May 2019*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Teaching assistant** \n'
                         '  *Environmental Fluid Mechanics* - Professor [J. Plazas](https://www.linkedin.com/in/jplazas)\n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Create deliverable workshops and grade them.'),
                html.Li('Assist students during question hours.'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2021 - Dec. 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Teaching assistant** \n'
                         '  *Geophysics* - Professor [I. Molina](https://www.linkedin.com/in/indira-molina-77123b40)\n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Create deliverable workshops and grade them.'),
                html.Li('Assist students during question hours.'),
            ])
        ], width=5)
    ], justify='center'),
    
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
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Responsible of the making of "Pilot study of Heavy Metal contamination in Avocado crops (Var. Hass)\n'
                        'and feasibility analysis of Crosscheck methodology in Heavy Metal distribution"'),
                html.Li('Support in the implementation of soil diagnostic services for agriculture (Nutricheck)'),
            ])
        ], width=5)
    ], justify='center'),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Nov. 2021 - Jan. 2022*', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Independent Professional on research project** \n'
                         '  **Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            dcc.Markdown('- Conducting and writing the paper of the study "Residential radon concentrations in Bogota and\n'
                         'neighbouring municipalities, Colombia: Results of an exploratory study" under the supervision\n' 
                         'of professor [C. Huguet](https://www.linkedin.com/in/carme-huguet-7769b991/)')
        ], width=5)
    ], justify='center'),
    
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            #### Personal
            * Analytical
            * Adaptable
            * Team worker
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            #### Programs
            * **Advanced:** Python, ArcGIS, QGIS
            * **Intrmediate:** R, LaTEX, Excel
            * **Basic:** AutoCAD, MatLAB
            ''')
        ], width=3),
        dbc.Col([
            dcc.Markdown('''
            #### Languages
            * **Spanish** - Native
            * **English** - Proficient (7.5/9 - IELTS)
            * **French** - Upper intermediate (C1 - DALF)
            ''')
        ], width=3)
    ], justify='center'),
])
