import requests
import json
from common.constants import rootRequest


class Utils:

    @staticmethod
    def formatList(countries):
        if len(countries) == 1:
            return countries
        elif len(countries) == 2:
            return f"{countries[0]} and {countries[1]}"
        else:
            output: str = ""
            for item in countries[:len(countries) - 2]:
                output += item + ", "
            output += "and " + countries[-1]
        return output

    @staticmethod
    def helperFunction():
        print(" ---- Functions ---- ")
        response = requests.get(rootRequest)
        text = json.dumps(response, sort_keys=True, indent=4)
        print(text)
