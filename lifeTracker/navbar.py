# Import Bootstrap from Dash
import os

import dash_bootstrap_components as dbc


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