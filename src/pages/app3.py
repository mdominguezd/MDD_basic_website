import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, title = 'AQ_Project')

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Air Quality monitoring and modeling in Bogotá, D.C., Colombia', style={'textAlign':'center'}),
                    html.Hr(),
                    dcc.Markdown("**Abstract:** Monitoring Air Quality (AQ) Networks are scarce in Latin America and when they exist they usually " 
                                 "consist of widely spread AQ stations that don't reflect the real distribution of AQ throughout the city. In this "
                                 "project I'm working with [Lucas Rivero Iribarne](https://www.lucasriveroiribarne.com/) to model AQ distribution "
                                 "in the city of Bogotá, Colombia by using remotely sensed information and Machine Learning algorithms",
                                 link_target='_blank'
                                 ),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])