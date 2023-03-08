import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    html.Div([],style = {'height':50}),
    dcc.Markdown('# Martín Domínguez Durán', style={'textAlign':'center'}),
    dcc.Markdown('**Wageningen, Netherlands**', style={'textAlign': 'center'}),
    html.Div([html.Img(src='../assets/FOTO_MDD_1.jpg', style = {'height' : 'auto', 'max-width' : 200, 'min-width': '10%', 'border-radius':'50%'})],
             style = {'textAlign' : 'center'}
            ),
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Col([dcc.Markdown('Environmental Engineer and Geoscientist from *Los Andes University, Bogotá, Colombia* and MSc Geo-Information student at\n'
                          '*Wageningen University & Research, The Netherlands*. I am a **dynamic**, **hardworking** and **curious** professional with a particular\n'
                          'interest in research topics involving environmental health, environmental modeling, data science, Geographic Information Systems\n'
                          'and Remote Sensing. I am passionate about making scientific research reproducible and accesible in non-scientfic contexts  by the\n'
                          'creation of interactive dashboards.\n',
                          style={'textAlign': 'center', 'white-space' : 'pre-wrap', 'font-family':'Arial'})]),
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
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap', 'bacground-color' : 'lightgray'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jan. 2018 - Dec. 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('B.Sc. Geoscientist (GPA: 4.45/5) \n'
                         '**Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Jul. 2017 - May 2021*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Minor in Photography \n'
                         '**Universidad de Los Andes** - Bogotá, Colombia',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    
    dbc.Row([
        dbc.Col([
            dcc.Markdown('*Aug. 2022 - present*',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('M.Sc. Geo-Information Science \n'
                         '**Wageningen University & Research** - Wageningen, Netherlands',
                         style={'white-space': 'pre-wrap'},
                         className='ms-3'),
        ], width=5)
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
    html.Div([],style = {'height' : 20}),
    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            #### Personal
            * Analytical
            * Adaptable
            * Curious
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            #### Programs
            * **Advanced:** Python, ArcGIS, QGIS
            * **Intrmediate:** R, LaTEX, Excel
            * **Basic:** AutoCAD, MatLAB, Bash
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
    ], justify='center', style = {'white-space' : 'pre-wrap'}),
])
