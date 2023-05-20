import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/app-aq"):
            name = 'Air Quality RS'
        elif page["path"].startswith("/app-ml"):
            name = 'Machine Learning course project'
        elif page["path"].startswith("/app-hear-n-now"):
            name = 'Hear and Now project'
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