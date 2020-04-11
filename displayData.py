from Utils import helperFunctions
import OnDataProcessing
import pandas as pd
import matplotlib.pyplot as plt


def plotGraph():
    plt.style.use('seaborn')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def plotGraphDF(country):
    dataframe = pd.read_csv('Outputs/' + country + '.csv')
    dataframe.plot()
    plotGraph()
    plt.show()


def compareCounties(countries, status):
    for country in countries:
        dataframe = pd.read_csv('Outputs/' + country + '.csv', index_col='Date')[status]
        plotGraph()
        dataframe.plot()
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()
