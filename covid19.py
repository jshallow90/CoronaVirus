import dash
import OnDataProcessing
import displayData
import machineLearning
from Utils import constants


def main():
    app = dash.Dash(__name__, external_stylesheets=constants.external_stylesheets)

    singleCountry = OnDataProcessing.getCountryData('united-kingdom')
    combinedCountry = OnDataProcessing.combineCountryDataFrames(constants.countryTestCases)
    countriesComparisonTables = OnDataProcessing.countriesComparisonTables(constants.countryTestCases)
    displayData.runServer(app, singleCountry, combinedCountry, countriesComparisonTables)

    return app


if __name__ == '__main__':
    app = main()
    app.run_server(debug=True)
