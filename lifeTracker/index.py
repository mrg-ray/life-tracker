# import dash-core, dash-html, dash io, bootstrap
import os

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Dash Bootstrap components
import dash_bootstrap_components as dbc
from flask_login import current_user, logout_user

from lifeTracker.data_store import DataStore
# Navbar, layouts, custom callbacks
from lifeTracker.navbar import Navbar, login, create, logout
from lifeTracker.manage_metrics import metric_layout
from lifeTracker.daily_tracker import tracker_form
from lifeTracker.reports import baseReportLayout, menuSlider

# Import app
from lifeTracker.trackerapp import app
# Import server for deployment
from lifeTracker.trackerapp import srv as server

user_id = None

app_name = os.getenv("DASH_APP_PATH", "/lifeTracker")

# Layout variables, navbar, header, content, and container
nav = Navbar()

header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H2(children="Life Tracker"),
                html.H3(children="A simple tool to manage your Life and Time better"),
            ]
        )
    ),
    className="banner",
)

content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])

container = dbc.Container([header, content])


# Menu callback, set and return
# Declare function  that connects other pages with content to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == '/create_user':
        return create
    if not current_user or not current_user.is_authenticated:
        return login
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout
        else:
            return logout
    user_id = current_user.id
    if pathname in [app_name, app_name + "/"]:
        return html.Div(
            [
                dcc.Markdown(
                    """
            ### The Applicaiton
            This application is a portfolio project built by [Matt Parra](https://devparra.github.io/) using Plotly's Dash,
            faculty.ai's Dash Bootstrap Components, and Pandas. Using historical MLB (Major League Baseball) data,
            this application provides visualizations for team and player statistics dating from 1903 to 2020. Selecting
            from a dropdown menu, the era will update the list of available teams and players in the range set on the years
            slider. The slider allows the user to adjust the range of years with which the data is presented.
            ### The Analysis
            The applicaiton breaks down each baseballs teams win/loss performance within a range of the teams history.
            Additionally, the application will break down the batting performance with the team batting average, BABIP, and strikeout
            rate. The application also brakes down the piching perfomance using the teams ERA and strikeout to walk ratio. Finally the feilding
            performance of each team is illustrated with total errors and double plays. The applicaiton will also breakdown
            each of teams players statistics within the given era.
            ### The Data
            The data used in this application was retrieved from [Seanlahman.com](http://www.seanlahman.com/baseball-archive/statistics/).
            Provided by [Chadwick Baseball Bureau's GitHub](https://github.com/chadwickbureau/baseballdatabank/) .
            This database is copyright 1996-2021 by Sean Lahman. This data is licensed under a Creative Commons Attribution-ShareAlike
            3.0 Unported License. For details see: [CreativeCommons](http://creativecommons.org/licenses/by-sa/3.0/)
        """
                ),
                html.Div([
                    html.Button("Export Data", id="btn_image"),
                    dcc.Download(id="download-image")
                ])
            ],
            className="home",
        )
    elif pathname.endswith("/metrics"):
        return metric_layout
    elif pathname.endswith("/tracker"):
        return tracker_form
    elif pathname.endswith("/reports"):
        return menuSlider, baseReportLayout
    else:
        return "ERROR 404: Page not found!"

@app.callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "./data_entry.db"
    )

# Main index function that will call and return all layout variables
def index():
    layout = html.Div([nav, container])
    return layout


# Set layout to index function
app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
