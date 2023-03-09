import dash_bootstrap_components as dbc
from .side_bar import sidebar

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, title = 'ML_Project')

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
                                    html.H3('Machine Learning course project', style={'textAlign':'center'}),
                                    html.Hr(),
                                    html.B('Abstract:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                    dcc.Markdown("When I followed the course Machine Learning during February and March 2023, I deeply enjoyed the programming of Machine Learning algorithms."
                                                 " However, I was always missing a visualization of the process that was being done. Therefore, I created an interactive dashboard where the user"
                                                 " can easily play with some parameters in regression, classificatiton and clustering alorithms to see the efffects on the output data. Click"
                                                 " [here](https://ml-mgi-project-dashboard.onrender.com) to checkout the results of the dashboard.",
                                                 link_target='_blank'
                                                 ),
                                    html.B('Overview:', style = {'font-family' : 'bahnschrift', 'font-size' : 20}),
                                    html.Div([html.Img(src='../assets/ML_dashboard.gif', style = {'max-width' : '80%', 'height':'auto'})],
                                                style = {'textAlign' : 'center'}
                                               ),
                                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
                        ]
                    )
                ], style = {'min-height':890})


