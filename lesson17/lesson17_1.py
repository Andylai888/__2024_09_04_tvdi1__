from dash import Dash,html,dcc
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div(
    [
    html.H1("Dash App的標題",style={"textAlign":'center'}),
    dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
    ])
    

if __name__ == '__main__':
    app.run(debug=True)