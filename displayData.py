import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import OnDataProcessing
from Utils import helperFunctions


def plotGraph():
    plt.style.use('seaborn')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def plotGraphDF(country):
    dataframe = OnDataProcessing.getCountryData(country)
    dataframe.plot()
    plotGraph()
    plt.show()


def compareCounties(countries, status):
    for country in countries:
        dataframe = OnDataProcessing.getCountryData(country)[status]
        plotGraph()
        dataframe.plot()
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range((len(dataframe)))
        ])
    ])


def runServer(app, singleCountryDataframe, allCountrysDataframe):
    app.layout = html.Div([
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure={
                'data': [
                    go.Scatter(
                        x=singleCountryDataframe[singleCountryDataframe[status] > 0].index,
                        y=singleCountryDataframe[singleCountryDataframe[status] > 0][status],
                        text=singleCountryDataframe[status],
                        mode='lines+markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=status
                    ) for status in ['deaths', 'confirmed', 'recovered']
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Total for Italy'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
        dcc.Graph(
            id='life-exp-vs-gdp',
            figure={
                'data': [
                    go.Scatter(
                        x=allCountrysDataframe[allCountrysDataframe['deaths'] > 0].index,
                        y=allCountrysDataframe[allCountrysDataframe['deaths'] > 0 and allCountrysDataframe['country'] == country]['deaths'],
                        text=singleCountryDataframe[status],
                        mode='lines+markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=status
                    ) for country in allCountrysDataframe.country.unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Total for Italy'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),

        html.Br(),
        html.Br(),

        generate_table(singleCountryDataframe)
    ])