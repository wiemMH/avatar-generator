import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash

from app import app, server

from apps import home
from transform import image_generator

server = app.server

import dash_bootstrap_components as dbc
import dash_html_components as html

dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("Home", header=True),
       
    ],
    label="Menu",
)

navbar = dbc.NavbarSimple(
    children=[
        #dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Home", header=True, href='#'),
                #dbc.DropdownMenuItem("Page 2", href="#"),
                #dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="My avatar",
    brand_href="#",
    color="primary",
    dark=True,
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return page1.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)