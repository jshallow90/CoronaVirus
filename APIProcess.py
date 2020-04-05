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


def countryDataRequest(country_slug, status):
    '''
    :param country_slug: country of the request from https://api.covid19api.com/countries
    :param status: can be one of deaths, confirmed, recovered
    :return: json of the requested country, mapped based on countryMapping function
    '''
    statuses = {'confirmed', 'recovered', 'deaths'}
    if status not in statuses:
        raise ValueError("Invalid status. Expected one of: %s" % statuses)

    provinceRequest = ""
    if country_slug in constants.UKSet:
        provinceRequest = country_slug
        country_slug = 'united-kingdom'
    elif country_slug in constants.FranceSet:
        provinceRequest = country_slug
        country_slug = 'france'

    requestPath = "{}country/{}/status/{}".format(constants.rootRequest, country_slug, status)
    response = requests.get(requestPath).json()

    if provinceRequest != "":
        provinceResponse = []
        for jsonObject in response:
            province = jsonObject['Province'] if 'Province' in jsonObject else ""
            if province.lower() == provinceRequest.lower():
                provinceResponse.append(jsonObject)
        response = provinceResponse
    elif country_slug in constants.countriesWithProvinces:
        countryResponse = []
        for jsonObject in response:
            province = jsonObject['Province'] if 'Province' in jsonObject else ""
            if province == "":
                countryResponse.append(jsonObject)
        response = countryResponse
    return response


def parseData(countryJSON, ignoreZeroDates=False):
    caseDict = {}
    for jsonObject in countryJSON:
        caseDate = datetime.datetime(int(jsonObject['Date'][:4]), int(jsonObject['Date'][5:7]),
                                     int(jsonObject['Date'][8:10]))
        numberCases = int(jsonObject['Cases'])
        if caseDate in caseDict:
            caseDict[caseDate] += numberCases
        elif ignoreZeroDates:
            if numberCases > 0:
                caseDict[caseDate] = numberCases
            else:
                continue
        else:
            caseDict[caseDate] = numberCases
    return caseDict


def plotGraph(dates, cases):
    plt.style.use('seaborn')
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def singleCountryStats(country, ignoreZeroDates=False):
    statuses = ['deaths', 'recovered', 'confirmed']
    for status in statuses:
        countryJSON = countryDataRequest(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=statuses)
    plt.show()


def compareCounties(countries, status, ignoreZeroDates=False):
    for country in countries:
        countryJSON = countryDataRequest(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + helperFunctions.formatList(countries))
    plt.show()


def main():
    # singleCountryStats('united-kingdom', ignoreZeroDates=True)
    compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'deaths', ignoreZeroDates=True)
    # helperFunctions.jprint(countryDataRequest('gibraltar', 'confirmed'))


if __name__ == '__main__':
    main()
