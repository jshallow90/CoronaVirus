from dataclasses import dataclass, field
import datetime
from typing import Dict
import requests
import pandas as pd
from common.database import Database
import common.constants as constants


@dataclass
class Country:
    name: str
    province: str = field(init=False, default=None)
    collection: str = field(init=False, default="countries")
    data: Dict = field(init=False, default=None)

    def __post_init__(self):
        if self.name not in constants.countrySlugs:
            raise ValueError(f'Country: {self.name} is not implemented')
        self.data = self.getCountryData()

    def json(self) -> Dict:
        return {
            "country": self.name
        }

    def getCountryData(self) -> Dict:
        """
        :return: dictionary of country will all statuses available in constants. dataframe will be of the format:
            key, datetime, province, deaths, confirmed, recovered
        """
        countryDict = {}

        for status in constants.statuses:
            requestPath = f"{constants.rootRequest}country/{self.name}/status/{status}"
            response = requests.get(requestPath).json()

            for jsonObject in response:
                if type(jsonObject) != dict:
                    continue
                year, month, day = (int(jsonObject['Date'][:4]), int(jsonObject['Date'][5:7]), int(jsonObject['Date'][8:10]))
                province = jsonObject['Province']
                key = f"{year}{month}{day}-{province}-{self.name}" if province != "" else f"{year}{month}{day}-{self.name}"
                numberCases = int(jsonObject['Cases'])

                if key in countryDict.keys():
                    countryDict[key][status] = numberCases
                else:
                    countryDict[key] = {
                        "date": datetime.datetime(year, month, day),
                        "country": self.name,
                        "province": jsonObject['Province'],
                        status: numberCases
                    }
        return countryDict

    def getCountryDF(self) -> pd.DataFrame:
        return pd.DataFrame.from_dict(self.data, orient='index')

    def saveToDB(self) -> None:
        data = {
            "country": self.name,
            "cases": self.getCountryData()
        }
        Database.update(self.collection, query=self.json(), data=data)

    def getByCounty(self):
        return Database.find_one(self.collection, self.json())
