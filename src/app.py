import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

import os
if 'yield_data' not in os.listdir():
    !git clone https://gist.github.com/3206e24244286dd25efd9e8bb39f079e.git yield_data

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LITERA])
server = app.server

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([dbc.NavLink(page["name"], href=page["path"])
                             for page in dash.page_registry.values()
                             if not page["path"].startswith("/app")
                            ])
            ])
        ],
        fluid=True,
    ),
    dark=True,
    color='#203442',
     style = {'width' : '100%','white-space' : 'pre-wrap'}
)

app.layout = dbc.Container([header, 
                            dash.page_container, 
                            html.Div([], style = {'height' :40, 'background' : '#203442'})], fluid=True, style = {'align':'center','width':"100%",'color' : '#0c1921', 'background-color' : '##ffffff'})

if __name__ == '__main__':
	app.run_server(port=8070)