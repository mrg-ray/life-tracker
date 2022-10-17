# Import Bootstrap from Dash
import os

import dash_bootstrap_components as dbc
from dash import html, dcc

app_name = os.getenv("DASH_APP_PATH", "/lifeTracker ")

# Navigation Bar function
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Manage Metrics", href=f"{app_name}/metrics")),
            dbc.NavItem(dbc.NavLink("Tracker Data", href=f"{app_name}/tracker")),
            dbc.NavItem(
                dbc.NavLink("Progress Report", href=f"{app_name}/reports")
            ),
        ],
        brand="Home",
        brand_href=f"{app_name}",
        sticky="top",
        color="light",
        dark=False,
        expand="lg",
    )
    return navbar

create = html.Div([html.H1('Create User Account')
                      , dcc.Location(id='create_user', refresh=True)
                      , dcc.Input(id="username"
                                  , type="text"
                                  , placeholder="user name"
                                  , maxLength=15)
                      , dcc.Input(id="password"
                                  , type="password"
                                  , placeholder="password")
                      , dcc.Input(id="email"
                                  , type="email"
                                  , placeholder="email"
                                  , maxLength=50)
                      , html.Button('Create User', id='submit-val', n_clicks=0)
                      , html.Div(id='container-button-basic')
                   ])  # end div
login = html.Div([dcc.Location(id='url_login', refresh=True)
                     , html.H2('''Please log in to continue:''', id='h1')
                     , dcc.Input(placeholder='Enter your username',
                                 type='text',
                                 id='uname-box')
                     , dcc.Input(placeholder='Enter your password',
                                 type='password',
                                 id='pwd-box')
                     , html.Button(children='Login',
                                   n_clicks=0,
                                   type='submit',
                                   id='login-button')
                     , html.Div(children='', id='output-state')
                  ])  # end div
success = html.Div([dcc.Location(id='url_login_success', refresh=True)
                       , html.Div([html.H2('Login successful.')
                                      , html.Br()
                                      , html.P('Select a Dataset')
                                      , dcc.Link('Data', href='/data')
                                   ])  # end div
                       , html.Div([html.Br()
                                      , html.Button(id='back-button', children='Go back', n_clicks=0)
                                   ])  # end div
                    ])  # end div

failed = html.Div([dcc.Location(id='url_login_df', refresh=True)
                      , html.Div([html.H2('Log in Failed. Please try again.')
                                     , html.Br()
                                     , html.Div([login])
                                     , html.Br()
                                     , html.Button(id='back-button', children='Go back', n_clicks=0)
                                  ])  # end div
                   ])  # end div
logout = html.Div([dcc.Location(id='logout', refresh=True)
                      , html.Br()
                      , html.Div(html.H2('You have been logged out - Please login'))
                      , html.Br()
                      , html.Div([login])
                      , html.Button(id='back-button', children='Go back', n_clicks=0)
                   ])  # end div
