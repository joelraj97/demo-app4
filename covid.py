import pandas as pd
import plotly.express as px  # (version 4.7.0)

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.read_csv("India_covaxin.csv")
dff = df[['date', 'total_vaccinations', 'people_fully_vaccinated']]
# fig = px.line(dff,x='date',y=['total_vaccinations','people_fully_vaccinated'])
# fig.show()

app.layout = html.Div([
    html.H1("Web Application Dashboards for Covid Vaccination India", style={'text-align': 'center'}),

    dcc.Checklist(id='my_option',
                  options=[
                      {'label': 'Total vaccination', 'value': 'total_vaccinations'},
                      {'label': 'People fully vaccinated', 'value': 'people_fully_vaccinated'},
                  ],
                  value=['total_vaccinations', 'people_fully_vaccinated'],
                  labelStyle={'display': 'inline-block'}
                  ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_vacc_map', figure={})
])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_vacc_map', component_property='figure')],
    [Input(component_id='my_option', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    # print(type(option_slctd))

    container = "The option was: {}".format(option_slctd)
    dff = df.copy()
    fig = px.line(dff, x='date', y=option_slctd)

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)