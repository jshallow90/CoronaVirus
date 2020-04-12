import dash
import OnDataProcessing
import displayData
import machineLearning
from Utils import constants
app = dash.Dash(__name__, external_stylesheets=constants.external_stylesheets)


def main(app):
    dataframe = OnDataProcessing.getCountryData('italy')
    displayData.runServer(app, dataframe)


if __name__ == '__main__':
    main(app)
    app.run_server(debug=True)
