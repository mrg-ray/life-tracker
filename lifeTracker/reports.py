# Menu slider used, NOT independent, MUST be used with main menu
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

menuSlider = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dcc.RangeSlider(
                    id="period-slider",
                    min=1,
                    max=24,
                    step=4,
                    tooltip={"always_visible": False, "placement": "bottom"},
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Adjust slider to desired range.",
                )
            )
        ),
    ],
    className="era-slider",
)


# Layout for Team Analysis page
baseReportLayout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3(children="Time Share"))),
        # Display Championship titles in datatable
        dbc.Row(
            dbc.Col(
                html.Div(id="team-data")
            ),
            justify="center",
        ),
        ### Graphs of Historical Team statistics ###
        dbc.Row(dbc.Col(html.H3(children="Team Analysis"))),
        # Bar Chart of Wins and Losses
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="wl-bar", config={"displayModeBar": False}),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 12, "offset": 0},
                lg={"size": 12, "offset": 0},
            )
        ),
        # Line Chart of Batting Average, BABIP, and Strikeout Rate
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="batting-line", config={"displayModeBar": False}),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 12, "offset": 0},
                lg={"size": 12, "offset": 0},
            )
        ),
        # Bar Char of Errors and Double Plays
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="feild-line", config={"displayModeBar": False}),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 12, "offset": 0},
                lg={"size": 12, "offset": 0},
            )
        ),
        dbc.Row(dbc.Col(html.H4(children="Pitching Performance"))),
        dbc.Row(
            [
                # Line graph of K/BB ratio with ERA bubbles
                dbc.Col(
                    dcc.Graph(id="pitch-bubble", config={"displayModeBar": False}),
                    xs={"size": 12, "offset": 0},
                    sm={"size": 12, "offset": 0},
                    md={"size": 12, "offset": 0},
                    lg={"size": 6, "offset": 0},
                ),
                # Pie Chart, % of Completed Games, Shutouts, and Saves of Total Games played
                dbc.Col(
                    dcc.Graph(id="pitch-pie", config={"displayModeBar": False}),
                    xs={"size": 12, "offset": 0},
                    sm={"size": 12, "offset": 0},
                    md={"size": 12, "offset": 0},
                    lg={"size": 6, "offset": 0},
                ),
            ],
            no_gutters=True,
        ),
    ],
    className="app-page",
)