import pandas as pd
from Utils import helperFunctions


def getCountryData(country):
    countryDataset = pd.read_csv(helperFunctions.csvTranslation(country), sep=',')  # check the csv file before to know that 'comma' here is ';'
    print(countryDataset.head(3))
    print(list(countryDataset.columns))  # show the features and label
    print(countryDataset.shape)  # instances vs features + label (4521, 17)
