import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Automobile Sales Dashboard"

# Sample data
data = {
    'Date': pd.date_range(start='1/1/2021', periods=12, freq='M'),
    'Sales': [100, 120, 130, 90, 85, 95, 105, 115, 110, 130, 120, 140]
}
df = pd.DataFrame(data)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Dashboard"),

    html.Label("Select Car Model:"),
    dcc.Dropdown(
        id='model-dropdown',
        options=[
            {'label': 'Model A', 'value': 'A'},
            {'label': 'Model B', 'value': 'B'},
            {'label': 'Model C', 'value': 'C'}
        ],
        value='A'  # Default value
    ),

    html.Label("Select Year:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': '2021', 'value': '2021'},
            {'label': '2022', 'value': '2022'},
            {'label': '2023', 'value': '2023'}
        ],
        value='2023'  # Default value
    ),

    html.Div(id='output-container', className='output-container'),

    dcc.Graph(id='recession-graph'),
    dcc.Graph(id='yearly-graph')
])

@app.callback(
    [Output('output-container', 'children'),
     Output('recession-graph', 'figure'),
     Output('yearly-graph', 'figure')],
    [Input('model-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_output(selected_model, selected_year):
    recession_fig = px.line(df, x='Date', y='Sales', title='Recession Report Statistics')
    yearly_fig = px.bar(df, x='Date', y='Sales', title='Yearly Report Statistics')
    return f'Selected Model: {selected_model}, Selected Year: {selected_year}', recession_fig, yearly_fig

if __name__ == '__main__':
    app.run_server(mode='inline')
