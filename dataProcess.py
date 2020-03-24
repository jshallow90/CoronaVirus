import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def getData():
    confirmed = pd.read_csv('Inputs/time_series-ncov-Confirmed.csv').set_index('Date')
    deaths = pd.read_csv('Inputs/time_series-ncov-Deaths.csv').set_index('Date')
    recovered = pd.read_csv('Inputs/time_series-ncov-recovered.csv').set_index('Date')
    return confirmed, deaths, recovered


def combineResults(confirmed, deaths, recovered):
    combined_results = pd.merge(confirmed[1:], deaths[1:],
                                on=['Date', 'Province/State', 'Country/Region', 'Lat', 'Long'])
    combined_results = pd.merge(combined_results, recovered[1:],
                                on=['Date', 'Province/State', 'Country/Region', 'Lat', 'Long'])
    combined_results = combined_results.rename(columns={
        'Province/State': 'Province',
        'Country/Region': 'Country',
        'Value_x': 'Number_Confirmed',
        'Value_y': 'Number_Killed',
        'Value': 'Number_Recovered'
    }).astype({
        'Province': 'str',
        'Country': 'str',
        'Lat': 'float',
        'Long': 'float',
        'Number_Confirmed': 'int64',
        'Number_Killed': 'int64',
        'Number_Recovered': 'int64'
    })
    return combined_results


def printResults(combined_results):
    colsToPlot = ['Number_Confirmed']  # , 'Number_Killed', 'Number_Recovered']
    countryList = ['Italy', 'Spain', 'United Kingdom', 'US', 'France', 'Germany', 'China']
    countryList = ['United Kingdom', 'France']
    regionList = ['', 'United Kingdom', 'France']
    combined_results = combined_results.set_index(pd.to_datetime(combined_results.index))
    combined_results = combined_results.loc[combined_results.Country.isin(countryList) & (combined_results.Province.isin(regionList) | combined_results.Province == "")]

    fig, ax = plt.subplots()
    combined_results.groupby('Country')[colsToPlot].plot(ax=ax, legend=False)

    plt.show()


def main():
    confirmed, deaths, recovered = getData()
    combinedDataset = combineResults(confirmed, deaths, recovered)
    printResults(combinedDataset)


if __name__ == '__main__':
    main()
