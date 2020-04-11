import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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


def showTable(dataframe):
    #fig = go.Figure(data=[go.Table(
    #    header=dict(values=list(dataframe.columns),
    #                fill_color='paleturquoise',
    #                align='center'),
    #    cells=dict(values=[dataframe.index, dataframe['deaths'], dataframe['confirmed'], dataframe['recovered']],
    #               fill_color='lavender',
    #               align='center'))
    #])
    fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                                   cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                          ])
    fig.show()
