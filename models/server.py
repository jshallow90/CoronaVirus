from dataclasses import dataclass, field
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from models.country import Country
from common import constants


@dataclass
class Server:
    countriesRequested = set()

    @staticmethod
    def runServer(app, country, countries):  # , countriesComparisonTables):
        countryDF = Server.getCountryDF(country)
        countriesDF = Server.getCountriesDF(countries)

        opts = [{'label': i, 'value': i} for i in constants.countrySlugs]
        opts = sorted(opts, key=lambda i: i['label'], reverse=False)
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
                            x=countryDF[countryDF[status] > 0].index,
                            y=countryDF[countryDF[status] > 0][status],
                            text=countryDF[status],
                            mode='lines+markers',
                            opacity=0.8,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name=status
                        ) for status in constants.statuses
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Date'},
                        yaxis={'title': 'Total for ' + countryDF['country'][0]},
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
                             value=[opts[77]['label'], opts[244]['label']],
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
                            x=countriesDF[
                                (countriesDF['deaths'] > 0) &
                                (countriesDF['country'] == country)
                                ].index,
                            y=countriesDF[
                                (countriesDF['deaths'] > 0) &
                                (countriesDF['country'] == country)
                                ]['deaths'],
                            text=country,
                            mode='lines+markers',
                            opacity=0.8,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name=country
                        ) for country in countriesDF.country.unique()
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Date'},
                        yaxis={'title': 'Total country comparison'},
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            ),

            html.Br(),
            html.Br(),

            # html.Div([
            #     dt.DataTable(
            #         id='comparison-data-table',
            #         columns=[{"name": i, "id": i} for i in countriesComparisonTables.columns],
            #         editable=False,
            #         style_table={'maxWidth': '1500px'},
            #         data=countriesComparisonTables.to_dict('records'),
            #     ),
            # ]),
        ])

        @app.callback(Output('single-country-graph', 'figure'), [Input('opt_single_country', 'value')])
        def updateSingleCountryTable(countryInput):
            _country = Country(countryInput)
            _countryDF = _country.getCountryDF()
            _countryDF = _countryDF[_countryDF['province'] == ''].set_index('date')

            fig = {
                'data': [
                    go.Scatter(
                        x=_countryDF[_countryDF[status] > 0].index,
                        y=_countryDF[_countryDF[status] > 0][status],
                        text=_countryDF[status],
                        mode='lines+markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=status
                    ) for status in constants.statuses
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Total for ' + countryDF['country'][0]},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
            return fig

        @app.callback(Output('country-comparison-graph', 'figure'), [Input('opt_combined_country', 'value')])
        def updateComparisonCountryTable(_countryList):
            _countriesDF = Server.getCountriesDF(_countryList)

            fig = {
                'data': [
                    go.Scatter(
                        x=_countriesDF[
                            (_countriesDF['deaths'] > 0) &
                            (_countriesDF['country'] == country)
                            ].index,
                        y=_countriesDF[
                            (_countriesDF['deaths'] > 0) &
                            (_countriesDF['country'] == country)
                            ]['deaths'],
                        text=country,
                        mode='lines+markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=country
                    ) for country in _countriesDF.country.unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'Date'},
                    yaxis={'title': 'Total country comparison'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
            return fig

        # @app.callback(Output('comparison-data-table', 'data'), [Input('opt_combined_country', 'value')])
        # def updateComparisonDatatable(countryList):
        #     combinedCountryDataframe = OnDataProcessing.compareCountryTables(countryList)
        #     data = combinedCountryDataframe.to_dict('records')
        #     return data

    @staticmethod
    def getCountryDF(country):
        countryClass = Country(country)
        countryDF = countryClass.getCountryDF()
        countryDF = countryDF[countryDF['province'] == ''].set_index('date')
        return countryDF

    @staticmethod
    def getCountriesDF(countryList):
        countriesDF = pd.DataFrame()
        for country in countryList:
            countryClass = Country(country)
            countryListDF = countryClass.getCountryDF()
            countryListDF = countryListDF[countryListDF['province'] == ''].set_index('date')
            countriesDF = countriesDF.append(countryListDF)
        return countriesDF
