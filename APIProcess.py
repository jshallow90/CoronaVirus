import requests
import json
import datetime
import matplotlib.pyplot as plt
rootRequest = "https://api.covid19api.com/"
plt.style.use('seaborn')

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
    print(countryJSON)
    dates = []
    cases = []
    for object in countryJSON:
        caseDate = datetime.datetime(int(object['Date'][:4]), int(object['Date'][5:7]), int(object['Date'][8:10]))
        numberCases = int(object['Cases'])
        dates.append(caseDate)
        cases.append(numberCases)
    return dates, cases


def plotGraph(dates, cases):
    plt.plot_date(dates, cases, linestyle='solid')
    plt.tight_layout()
    plt.gcf().autofmt_xdate()
    plt.show()


def main():
    # helperFunction()
    countryJSON = countryStatus("spain", "confirmed")
    dates, cases = parseData(countryJSON)
    plotGraph(dates, cases)


if __name__ == '__main__':
    main()

