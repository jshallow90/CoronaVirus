import requests
import json
import datetime
import matplotlib.pyplot as plt

rootRequest = "https://api.covid19api.com/"
plt.style.use('seaborn')


def formatList(list):
    output = ""
    if len(list) > 1:
        for item in list[:len(list)-2]:
            output += item + ", "
        output += "and " + list[-1]
    else:
        output = list
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


def parseData(countryJSON):
    caseDict = {}
    for object in countryJSON:
        caseDate = datetime.datetime(int(object['Date'][:4]), int(object['Date'][5:7]), int(object['Date'][8:10]))
        numberCases = int(object['Cases'])
        if caseDate in caseDict:
            caseDict[caseDate] += numberCases
        else:
            caseDict[caseDate] = numberCases
    return caseDict


def plotGraph(dates, cases):
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.gcf().autofmt_xdate()


def singleCountryStats(country):
    statuses = ['confirmed', 'recovered', 'deaths']
    for status in statuses:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=statuses)


def compareCounties(countries, status):
    for country in countries:
        countryJSON = countryStatus(country, status)
        cases = parseData(countryJSON)
        plotGraph(cases.keys(), cases.values())
    plt.legend(labels=countries)
    plt.title(status.capitalize() + " total for countries : " + formatList(countries))


def main():
    #singleCountryStats('italy')
    compareCounties(['us', 'italy'], 'deaths')
    plt.show()


if __name__ == '__main__':
    main()

