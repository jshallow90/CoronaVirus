import dash
import OnDataProcessing
import displayData
import machineLearning
from Utils import constants


def main():
    app = dash.Dash(__name__, external_stylesheets=constants.external_stylesheets)
    displayData.runServer(app, OnDataProcessing.getCountryData('italy'),
                          OnDataProcessing.combineCountryDataFrames(constants.countryTestCases))
    return app


if __name__ == '__main__':
    app = main()
    app.run_server(debug=True)
