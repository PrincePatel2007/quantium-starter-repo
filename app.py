from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import csv
import datetime

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
data = []

with open(INPUT_FILE, 'r') as file:  # SUGGESTED EDIT APPLIED HERE
    reader = csv.reader(file)
    next(reader)  # Skip header if there is one
    for row in reader:
        sales = float(row[0])
        date = datetime.datetime.strptime(row[1], '%Y-%m-%d').date()
        region = row[2]
        data.append({"date": date, "sales": sales, "region": region})

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

print(df[0:20]) #For debugging purposes

# 2. Define the Layout (What the user sees)
app.layout = html.Div([
    html.H1("Pink Morsel Visualizer", style={"textAlign": "center"}),
    
    # Dropdown menu component
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r.capitalize(), "value": r} for r in df["region"].unique()],
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
    # Filter dataset based on dropdown choice
    filtered_df = df[df["region"] == selected_region]
    
    # Create an updated line graph using Plotly Express
    fig = px.line(filtered_df, x="date", y="sales", title=f"Sales Timeline - {selected_region}")
    return fig

# 4. Run the Server
if __name__ == "__main__":
    app.run(debug=True)