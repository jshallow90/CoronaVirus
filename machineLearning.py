import pandas as pd
from OnDataProcessing import countryCSVReader

def getCountryData(country):
    countryDataset = countryCSVReader(country) # check the csv file before to know that 'comma' here is ';'
    print(countryDataset.head(3))
    print(list(countryDataset.columns))  # show the features and label
    print(countryDataset.shape)  # instances vs features + label (4521, 17)
