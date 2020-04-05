import json
import requests
from Utils import constants
import sys


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
    response = requests.get(constants.rootRequest)
    jprint(response.json())


def printOutput(outputFile, inputJSON):
    outputPath = "Outputs/" + outputFile
    sys.stdout = open(outputPath, "w")
    jprint(inputJSON)
