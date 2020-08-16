from dataclasses import dataclass, field
import datetime
import requests
import pandas as pd
from common.database import Database
import common.constants as constants


@dataclass
class Country:
    country: str
    province: str = field(init=False, default=None)

    def __post_init__(self):
        if self.country not in constants.countrySlugs:
            raise ValueError(f'Country: {self.country} is not implemented')
        return True

    def getCountryData(self):
        """
        :return: dataframe of country will all statuses available in constants. dataframe will be of the format:
            key, datetime, province, deaths, confirmed, recovered
        """
        countryDict = {}

        for status in constants.statuses:
            requestPath = f"{constants.rootRequest}country/{self.country}/status/{status}"
            response = requests.get(requestPath).json()

            for jsonObject in response:
                if type(jsonObject) != dict:
                    continue
                year, month, day = (int(jsonObject['Date'][:4]), int(jsonObject['Date'][5:7]), int(jsonObject['Date'][8:10]))
                province = jsonObject['Province']
                key = f"{year}{month}{day}-{province}-{self.country}" if province != "" else f"{year}{month}{day}-{self.country}"
                numberCases = int(jsonObject['Cases'])

                if key in countryDict.keys():
                    countryDict[key][status] = numberCases
                else:
                    countryDict[key] = {
                        "date": datetime.datetime(year, month, day),
                        "country": self.country,
                        "province": jsonObject['Province'],
                        status: numberCases
                    }
        return pd.DataFrame.from_dict(countryDict, orient='index')
