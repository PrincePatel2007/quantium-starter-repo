from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd


INPUT_FILE = 'data/filtered_sales_data.csv'

# 1. Initialize the Dash App
app = Dash(__name__)

# Mock data to simulate filtered sales data
'''data = {
    "date": ["2026-01-01", "2026-01-02", "2026-01-01", "2026-01-02"],
    "sales": [100, 150, 80, 120],
    "region": ["north", "north", "south", "south"]
}'''

# With real data
df = pd.read_csv(INPUT_FILE)
df = df.sort_values(by="date")


print(df[0:20]) #For debugging purposes

# 2. Define the Layout (What the user sees)
app.layout = html.Div([
    html.H1("Pink Morsel Visualizer", style={"textAlign": "center"}),
    
    # Dropdown menu component
    dcc.Dropdown(
        id="region-dropdown",

        options= [
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
            {"label": "All Regions", "value": "all"}
        ],

        value="north", # Default value
        clearable=False
    ),
    
    # Graph component
    dcc.Graph(id="sales-line-chart")
])

# 3. Define the Callbacks (The interactivity)
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-dropdown", "value")
)
def update_graph(selected_region):

    if selected_region=='all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == selected_region]
    
    # Create an updated line graph using Plotly Express
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales Timeline - {selected_region.capitalize()}")
    return fig

# 4. Run the Server
if __name__ == "__main__":
    app.run(debug=True)