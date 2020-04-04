import requests
import json
import datetime
import matplotlib.pyplot as plt

rootRequest = "https://api.covid19api.com/"
plt.style.use('seaborn')


def formatList(list):
    output = ""
    if len(list) == 1:
        output = list
    elif len(list) == 2:
        output += list[0] + " and " + list[1]
    elif len(list) > 2:
        for item in list[:len(list) - 2]:
            output += item + ", "
        output += "and " + list[-1]
    return output


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def helperFunction():
    print(" ---- Functions ---- ")
    response = requests.get(rootRequest)
    jprint(response.json())


def countryStatus(country_slug, status):
    requestPath = ""
    if status in {'confirmed', 'recovered', 'deaths'}:
        requestPath = "{}country/{}/status/{}".format(rootRequest, country_slug, status)
    response = requests.get(requestPath)
    return response.json()


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
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.yscale("log", basey=2)
    plt.gcf().autofmt_xdate()


def singleCountryStats(country, ignoreZeroDates=False):
    statuses = ['deaths', 'recovered', 'confirmed']
    for status in statuses:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=statuses)
    plt.show()


def compareCounties(countries, status, ignoreZeroDates=False):
    for country in countries:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON, ignoreZeroDates)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + formatList(countries))
    plt.show()


def main():
    singleCountryStats('united-kingdom', ignoreZeroDates=True)
    #compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'deaths', ignoreZeroDates=True)


if __name__ == '__main__':
    main()
