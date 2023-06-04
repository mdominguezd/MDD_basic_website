import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SANDSTONE, dbc.icons.BOOTSTRAP])
server = app.server


header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.Col([
                    html.Img(src='assets/favicon.ico', height="40px"),
                    dbc.NavbarBrand(" Martín Domínguez Durán", className="ms-2")
                ],
                    align = 'start',
                    width={"size":"auto"}
                ),
            ]),
            
            dbc.Row([
                dbc.Col(
                    dbc.Nav([dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
                             for page in dash.page_registry.values()
                             if not page["path"].startswith("/app")
                            ], 
                            navbar = True),
                    align = 'start',
                    width={"size":"auto"}
                ),
            ], align = 'center'),
            
             dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
                
            dbc.Row([
                dbc.Col(
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink(html.I(className="bi-github"), href="https://github.com/mdominguezd",external_link=True) ),
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/in/mart%C3%ADn-dom%C3%ADnguez-dur%C3%A1n-54b4681b6/",external_link=True))
                    ], navbar=True
                    ),
                    align = 'center',
                    width={"size":"auto"}
                )
            ], align = 'center')
        ],
        fluid=True,
    ),
    dark=True,
    color='#203442',
    # style = {'width' : '100%','margin' : 'auto'}
)


app.layout = html.Div([header, 
                       dash.page_container, 
                       html.Div([], style = {'height' :40,
                                             'background' : '#203442'})], 
                      # fluid=True, 
                      style = {'align':'center',
                               'width':"100%",
                               'margin' : 'auto',
                               'color' : '#0c1921',
                               'background-color' : '##ffffff'})


if __name__ == '__main__':
	app.run_server(port=8090)