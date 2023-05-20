import dash_bootstrap_components as dbc
from .side_bar import sidebar

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, title = 'Hear_and_Now')

def layout():
    return html.Div([html.Div([], style = {'height':30}),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    sidebar()
                                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                            dbc.Col(
                                [
                                    html.H3('Hear and Now: Interactive web application for bird diversity education', style={'textAlign':'center'}),
                                    html.Hr(),
                                    html.B('Abstract:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                    dcc.Markdown("Visit the dashboard [here](http://hearandnow.eu.pythonanywhere.com/).",
                                                 link_target='_blank'
                                                 ),
                                    html.B('Overview:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                    html.Div([html.Img(src='../assets/Hear_n_Now.gif', style = {'max-width' : '80%', 'height':'auto'})],
                                                style = {'textAlign' : 'center'}
                                               ),
                                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
                        ]
                    )
                ], style = {'min-height':890})
