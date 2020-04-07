from Utils import helperFunctions
import OnDataProcessing
import matplotlib.pyplot as plt


def plotGraph(dates, cases):
    plt.style.use('seaborn')
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def singleCountryStats(country, ignoreZeroDates=False):
    statuses = ['deaths', 'recovered', 'confirmed']
    deathData = OnDataProcessing.countryDataRequest(country, 'deaths')
    confirmedData = OnDataProcessing.countryDataRequest(country, 'confirmed')
    recoveredData = OnDataProcessing.countryDataRequest(country, 'recovered')
    combinedData = OnDataProcessing.combineCountryStatistics(country, deathData, confirmedData, recoveredData)
    #for status in statuses:
    #    countryJSON = OnDataProcessing.countryDataRequest(country, status)
    #    cases = OnDataProcessing.parseData(countryJSON, ignoreZeroDates)
    #    plotGraph(cases.keys(), cases.values())
    combinedData.plot()
    #plt.legend(labels=statuses)
    plt.show()


def compareCounties(countries, status, ignoreZeroDates=False):
    for country in countries:
        countryJSON = OnDataProcessing.countryDataRequest(country, status)
        cases = OnDataProcessing.parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()


def main():
    singleCountryStats('united-states', ignoreZeroDates=True)
    # compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'deaths', ignoreZeroDates=True)
    USADeaths = (OnDataProcessing.parseData(OnDataProcessing.countryDataRequest('united-states', 'deaths'), True))
    USAConfirmed = (OnDataProcessing.parseData(OnDataProcessing.countryDataRequest('united-states', 'confirmed'), True))
    USARecovered = (OnDataProcessing.parseData(OnDataProcessing.countryDataRequest('united-states', 'recovered'), True))
    OnDataProcessing.combineCountryStatistics('united-states', USADeaths, USAConfirmed, USARecovered)
    # helperFunctions.jprint(countryDataRequest('gibraltar', 'confirmed'))


if __name__ == '__main__':
    main()
