import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/app3"):
            name = 'Air Quality RS'
        elif page["path"].startswith("/app2"):
            name = 'Machine Learning course project'
        else:
            name = page['path']
        if page["path"].startswith("/app"):
            nav_links.append(
                dbc.NavLink(
                    [
                            html.Div(name, className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/projects":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Rn Modeling project", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
    return html.Div([html.H3('Projects'),
                     html.Hr(),
                     dbc.Nav(children=nav_links,
                             vertical=True,
                             pills=True)
                    ])
                   # className="bg-dark")