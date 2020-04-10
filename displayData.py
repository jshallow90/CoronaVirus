from Utils import helperFunctions
import OnDataProcessing
import matplotlib.pyplot as plt


def plotGraph(dates, cases):
    plt.style.use('seaborn')
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def plotGraphDF(dataframe):
    plt.style.use('seaborn')
    dataframe.plot()
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()
    plt.show()


def singleCountryStats(country):
    statuses = ['deaths', 'confirmed', 'recovered']
    dataList = []
    for status in statuses:
        dataList.append(OnDataProcessing.parseData(OnDataProcessing.countryDataRequest(country, status), True))
    combinedData = OnDataProcessing.combineCountryStatistics(country, dataList, True)
    plotGraphDF(combinedData)


def compareCounties(countries, status, ignoreZeroDates=False):
    for country in countries:
        countryJSON = OnDataProcessing.countryDataRequest(country, status)
        cases = OnDataProcessing.parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()


def main():
    singleCountryStats('united-states')
    # compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'deaths', ignoreZeroDates=True)


if __name__ == '__main__':
    main()
