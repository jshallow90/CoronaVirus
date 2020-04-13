from Utils import constants
import requests
import datetime
import pandas as pd
import os.path


class Country:
    """
    Defines country class holding dates and totals as list objects.
    """

    def __init__(self, country, dates, totalDeaths, totalConfirmed, totalRecovered):
        self.country = country
        self.dates = dates
        self.totalDeaths = totalDeaths
        self.totalConfirmed = totalConfirmed
        self.totalRecovered = totalRecovered

    def appendData(self, date, deathCount, confirmedCount, recoveredCount):
        self.dates.append(date)
        self.totalDeaths.append(deathCount)
        self.totalConfirmed.append(confirmedCount)
        self.totalRecovered.append(recoveredCount)


def isValidCountry(country):
    if country in constants.countrySlugs:
        return True
    return False


def countryDataRequest(country_slug, status):
    """
    :param country_slug: country of the request from https://api.covid19api.com/countries
    :param status: can be one of deaths, confirmed, recovered
    :return: json of the requested country, mapped based on countryMapping function
    """
    statuses = constants.statuses
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


def singleCountryStatistics(country, printCSV=False):
    """
    :param country: country requesting data for
    :param deaths: parseData for country for number of deaths
    :param confirmed: parseData for country for number of confirmed cases
    :param recovered: parseData for country for number of recovered cases
    :param printCSV: boolean whether to print the data to a CSV file
    :return: format will be
    datetime, deaths, confirmed, recovered
    """
    dataList = []
    for status in constants.statuses:
        dataList.append(pd.Series(parseData(countryDataRequest(country, status)), name=status))
    combined_fd = pd.concat(dataList, axis=1)
    combined_fd['country'] = country
    combined_fd.index.names = ['Date']

    if printCSV:
        outputFilePath = 'Outputs/' + country + '.csv'
        combined_fd.to_csv(outputFilePath, index=True, header=True)
    return combined_fd


def countryCSVReader(countryName):
    parsedFilename = 'Outputs/' + countryName + '.csv'
    df = pd.read_csv(parsedFilename, sep=',')
    df = df.set_index('Date')
    return df


def requiresAPIupdate(countryName):
    if countryName is None:
        return False
    parsedFilename = 'Outputs/' + countryName + '.csv'
    if not os.path.isfile(parsedFilename):
        return True
    else:
        currentDate = datetime.datetime.today()
        countryDate = max(countryCSVReader(countryName).index)
        countryDateParsed = datetime.datetime(int(countryDate[:4]), int(countryDate[5:7]), int(countryDate[8:10]))
        return (currentDate - countryDateParsed).days > 1


def getCountryData(countryName):
    """
    :param countryName:
    :return: returns pandas data frame from either CSV if no update is required, or from API request if this is the
    first time running the request today
    """
    if not isValidCountry:
        raise ValueError("Invalid country slug. must be one of : " + constants.countrySlugs)

    if requiresAPIupdate(countryName):
        return singleCountryStatistics(countryName, True)
    else:
        return countryCSVReader(countryName)


def combineCountryDataFrames(countries):
    countriesDataFrames = pd.DataFrame()
    for country in countries:
        countriesDataFrames = countriesDataFrames.append(getCountryData(country))
    return countriesDataFrames


def countriesComparisonTables(countries):
    cols = [
            'country', 'confirmed', 'deaths', 'recovered',
            'Change in deaths cases in 1 day', 'Change in deaths cases in one week',
            'Change in confirmed cases in 1 day', 'Change in confirmed cases in one week',
            'Change in recovered cases in 1 day', 'Change in recovered cases in one week'
            ]
    countriesComparisonTables = pd.DataFrame(columns=cols)
    for country in countries:
        countryDF = getCountryData(country)
        countriesComparisonTables = countriesComparisonTables.append(countryDF.iloc[-1])

        for status in constants.statuses:
            oneDayDelta = countryDF.iloc[-1][status] - countryDF.iloc[-2][status]
            weekDelta = countryDF.iloc[-1][status] - countryDF.iloc[-8][status]
            countriesComparisonTables.iloc[
                -1, countriesComparisonTables.columns.get_loc('Change in ' + status + ' cases in 1 day')] = oneDayDelta
            countriesComparisonTables.iloc[
                -1, countriesComparisonTables.columns.get_loc('Change in ' + status + ' cases in one week')] = weekDelta

    countriesComparisonTables['country'] = countriesComparisonTables['country'].str.title()
    return countriesComparisonTables
