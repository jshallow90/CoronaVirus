import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import OnDataProcessing
from Utils import helperFunctions, constants


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


def runServer(app, singleCountryDataframe, allCountrysDataframe, countriesComparisonTables):
    opts = [{'label': i, 'value': i} for i in constants.countrySlugs]
    opts = sorted(opts, key = lambda i: i['label'], reverse=False)
    app.layout = html.Div([
        html.H2('COVID-19 outbreak analysis'),
        html.Br(),
        html.H4('Single country display'),

        # dropdown single country
        html.P([
            html.Label("Choose a country"),
            dcc.Dropdown(id='opt_single_country', options=opts,
                         value=opts[244]['label'])
            ], style={'width': '400px',
                  'fontSize': '20px',
                  'padding-left': '10px',
                  'display': 'inline-block'}),
        dcc.Graph(
            id='single-country-graph',
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
                    yaxis={'title': 'Total for ' + singleCountryDataframe['country'][0]},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),

        html.Br(),
        html.H4('Country comparison'),

        # dropdown country comparison
        html.P([
            html.Label("Choose a set of countries"),
            dcc.Dropdown(id='opt_combined_country', options=opts,
                         value=[opts[244]['label'], opts[246]['label']],
                         multi=True)
        ], style={'width': '400px',
                  'fontSize': '20px',
                  'padding-left': '10px',
                  'display': 'inline-block'}),

        dcc.Graph(
            id='country-comparison-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=allCountrysDataframe[
                            (allCountrysDataframe['deaths'] > 0) &
                            (allCountrysDataframe['country'] == country)
                        ].index,
                        y=allCountrysDataframe[
                            (allCountrysDataframe['deaths'] > 0) &
                            (allCountrysDataframe['country'] == country)
                            ]['deaths'],
                        text=country,
                        mode='lines+markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=country
                    ) for country in allCountrysDataframe.country.unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Date'},
                    #yaxis={'type': 'log', 'dtick': 'log_10(2)', 'title': 'Total country comparison'},
                    yaxis={'title': 'Total country comparison'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),

        html.Br(),
        html.Br(),

        html.Div([
            dash_table.DataTable(
                id='comparison-data-table',
                columns=[{"name": i, "id": i} for i in countriesComparisonTables.columns],
                editable=False,
                style_table={'maxWidth': '1500px'},
                data=countriesComparisonTables.to_dict('records'),
            ),
        ]),
    ])

    @app.callback(Output('single-country-graph', 'figure'), [Input('opt_single_country', 'value')])
    def updateSingleCountryTable(countryInput):
        singleCountryDataframe = OnDataProcessing.getCountryData(countryInput)
        fig = {
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
                yaxis={'title': 'Total for ' + singleCountryDataframe['country'][0]},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
        return fig

    @app.callback(Output('country-comparison-graph', 'figure'), [Input('opt_combined_country', 'value')])
    def updateComparisonCountryTable(countryList):
        combinedCountryDataframe = OnDataProcessing.combineCountryDataFrames(countryList)
        fig = {
            'data': [
                go.Scatter(
                    x=combinedCountryDataframe[
                        (combinedCountryDataframe['deaths'] > 0) &
                        (combinedCountryDataframe['country'] == country)
                    ].index,
                    y=combinedCountryDataframe[
                        (combinedCountryDataframe['deaths'] > 0) &
                        (combinedCountryDataframe['country'] == country)
                    ]['deaths'],
                    text=country,
                    mode='lines+markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=country
                ) for country in combinedCountryDataframe.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                #yaxis={'type': 'log', 'dtick': 'log_10(2)', 'title': 'Total country comparison'},
                yaxis={'title': 'Total country comparison'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
        return fig

    @app.callback(Output('comparison-data-table', 'data'), [Input('opt_combined_country', 'value')])
    def updateComparisonDatatable(countryList):
        combinedCountryDataframe = OnDataProcessing.countriesComparisonTables(countryList)
        data = combinedCountryDataframe.to_dict('records')
        return data
