import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__, title='RnProject', order=2)

def layout():
    return html.Div([html.Div([], style = {'height':30}),
                     dbc.Row([dbc.Col([sidebar()],
                                      xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                              dbc.Col([html.H3('Development of Indoor Rn modeling app', style={'textAlign':'center'}),
                                       html.Hr(),
                                       html.B('Abstract:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                       dcc.Markdown('Radon (222Rn) is a naturally occurring gas that represents a health threat due to its causal\n'
                                                    'relationship with lung cancer. Despite its potential health impacts, few studies have been carried out to\n'
                                                    'assess this public health problem in countries where RC measurements and research are scarce. This project aims\n'
                                                    'to contribute to the bridging of the baseline information gap by using inferential statistic methods to estimate\n'
                                                    'indoor RC spatial distribution and building an easy-to-use [webapp](ircmodelingdashboard.eu.pythonanywhere.com/) for RC modeling.', link_target='_blank'),
                                       html.B('Overview:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                       html.Div([html.Img(src='../assets/RN_dashboard.gif', style = {'max-width' : '70%', 'height':'auto'})],
                                                style = {'textAlign' : 'center'}
                                               ),
                                      ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
                             ])
                    ],
                    style = {'min-height':890})
