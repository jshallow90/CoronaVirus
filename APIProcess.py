import constants
import helperFunctions
import requests
import datetime
import matplotlib.pyplot as plt


class Country:
    def __init__(self, country):
        self.country = country
        self.dates = []
        self.totals = []

    def appendData(self, date, count):
        self.dates.append(date)
        self.totals.append(count)


def countryStatus(country_slug, status):
    requestPath = ""
    if status in {'confirmed', 'recovered', 'deaths'}:
        requestPath = "{}country/{}/status/{}".format(constants.rootRequest, country_slug, status)
    response = requests.get(requestPath)
    return response.json()


def parseData(countryJSON, ignoreZeroDates=False):
    # caseDict = {}
    for jsonObject in countryJSON:
        country = jsonObject['Country']
        province = jsonObject['Province'] if 'Province' in jsonObject else ""
        caseDate = datetime.datetime(int(jsonObject['Date'][:4]), int(jsonObject['Date'][5:7]),
                                     int(jsonObject['Date'][8:10]))
        numberCases = int(jsonObject['Cases'])

        if province == "" and country == "United Kingdom":
            pass
        elif country == "United Kingdom":
            country = province

        countryList = [item.country for item in constants.countryClasses]
        if country not in countryList:
            newCountry = Country(country)
            if ignoreZeroDates:
                if numberCases > 0:
                    newCountry.appendData(caseDate, numberCases)
                    constants.countryClasses.append(newCountry)
            else:
                newCountry.appendData(caseDate, numberCases)
                constants.countryClasses.append(newCountry)
        else:
            constants.countryClasses[countryList.index(country)].appendData(caseDate, numberCases)
    return constants.countryClasses


def plotGraph(dates, cases):
    plt.style.use('seaborn')
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def singleCountryStats(country, ignoreZeroDates=False):
    statuses = ['deaths', 'recovered', 'confirmed']
    #statuses = ['confirmed']
    countryCount = 0
    countryLegend = []
    for status in statuses:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        for country in cases:
            print(country.country + " " + str(country.dates) + " " + str(country.totals))
            plotGraph(country.dates, country.totals)
            countryCount += 1
            countryLegend.append(country.country)
    ## needs redoing
    if countryCount > 1:
        plt.legend(labels=[statuses, countryLegend])
    else:
        plt.legend(labels=statuses)
    plt.show()


def compareCounties(countries, status, ignoreZeroDates=False):
    for country in countries:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()


def main():
    singleCountryStats('united-kingdom', ignoreZeroDates=True)
    # compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'confirmed', ignoreZeroDates=True)
    # helperFunctions.printOutput('United-Kingdom.json', countryStatus('united-kingdom', 'deaths'))


if __name__ == '__main__':
    main()
