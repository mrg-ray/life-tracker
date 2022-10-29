import os
import warnings

import configparser
# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
from dash import Output, Input, State, html, dcc
from flask_login import LoginManager, login_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table

from lifeTracker.data_store import DataStore
from lifeTracker.navbar import login

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Life Tracker"
# set app server to variable for deployment
srv = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# config
srv.config.update(
    SECRET_KEY=os.urandom(12),
)
# db = SQLAlchemy()
# db.init_app(srv)

login_manager = LoginManager()
login_manager.init_app(srv)
login_manager.login_view = '/login'


warnings.filterwarnings("ignore")

config = configparser.ConfigParser()

#
# # User as base
# Users_tbl = Table('users', Users.metadata)
# Users_tbl.metadata.create_all(db_engine)

# Create User class with UserMixin

class Users(UserMixin):
    id=None
    name=None
    pass
ds=DataStore()
# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    user = ds.getUserById(user_id)
    userObj = Users()
    userObj.id = user[0][0]
    userObj.name = user[0][1]
    return userObj


@app.callback(
    [Output('container-button-basic', "children")]
    , [Input('submit-val', 'n_clicks')]
    , [State('username', 'value'), State('password', 'value'), State('email', 'value')])
def insert_users(n_clicks, un, pw, em):
    if n_clicks == 0:
        return
    if un is not None and pw is not None and em is not None:
        ins = ds.createUser(username=un, password=pw, email=em, )
        return [login]
    else:
        return [html.Div([html.H2('Already have a user account?'), dcc.Link('Click here to Log In', href='/login')])]


@app.callback(
    Output('url_login', 'pathname')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def successful(n_clicks, input1, input2):
    if not n_clicks:
        pass
    user = ds.getUserByName(input1)
    if len(user) > 0:
        if user[0][3] == input2:
            userObj = Users()
            userObj.id = user[0][0]
            login_user(userObj)
            return '/tracker'
        else:
            pass
    else:
        return '/logout'


@app.callback(
    Output('output-state', 'children')
    , [Input('login-button', 'n_clicks')]
    , [State('uname-box', 'value'), State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = ds.getUserByName(input1)
        if len(user) > 0:
            if user[0][3] == input2:
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''


@app.callback(
    Output('url_login_success', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'


@app.callback(
    Output('url_login_df', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'


# Create callbacks
@app.callback(
    Output('url_logout', 'pathname')
    , [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'
