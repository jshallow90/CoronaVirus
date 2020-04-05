import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


def getData():
    confirmed = pd.read_csv('../Inputs/time_series-ncov-Confirmed.csv').set_index('Date')
    deaths = pd.read_csv('../Inputs/time_series-ncov-Deaths.csv').set_index('Date')
    recovered = pd.read_csv('../Inputs/time_series-ncov-Recovered.csv').set_index('Date')
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
    combined_results['Mapped_Country'] = combined_results.apply(lambda row: defineCountry(row), axis=1)
    return combined_results


def defineCountry(row):
    province = row['Province']
    country = row['Country']
    if country == "United Kingdom":
        UKProvinces = ['Bermuda', 'Cayman Islands', 'Channel Islands', 'Gibraltar', 'Isle of Man', 'Montserrat']
        if province in UKProvinces:
            return "UK - " + province
    elif country == 'France':
        FranceProvinces = ['French Guiana', 'French Polynesia', 'Guadeloupe', 'Mayotte', 'New Caledonia', 'Reunion', 'Saint Barthelemy', 'St Martin']
        if province in FranceProvinces:
            return "FR - " + province
    return country


def plotGraph(combined_results):
    colsToPlot = ['Number_Confirmed']  # , 'Number_Killed', 'Number_Recovered']
    countryList = ['Italy', 'Spain', 'United Kingdom', 'US', 'France', 'Germany', 'China']
    countryList = ['Italy', 'Spain', 'United Kingdom', 'France', 'Germany']
    combined_results = combined_results.set_index(pd.to_datetime(combined_results.index))
    combined_results = combined_results.loc[combined_results.Mapped_Country.isin(countryList)]

    fig, ax = plt.subplots()
    graphToPlot = combined_results.groupby('Country')[colsToPlot]
    graphToPlot.plot(ax=ax, legend=True, label='Country')
    plt.show()


def printGlobe(df, columnToPlot):
    fig = px.scatter_geo(df, locations="Mapped_Country")
    fig.show()


def main():
    confirmed, deaths, recovered = getData()
    combinedDataset = combineResults(confirmed, deaths, recovered)
    #plotGraph(combinedDataset)
    printGlobe(combinedDataset, "Number_Confirmed")


if __name__ == '__main__':
    main()