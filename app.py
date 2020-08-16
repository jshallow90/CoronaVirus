from dash import Dash
from models import displayData
from models.country import Country
from common import constants


def main():
    app = Dash(__name__, external_stylesheets=constants.external_stylesheets)

    startingCountry = Country('united-kingdom')
    combinedCountries = [Country('united-kingdom'), Country('italy'), Country('spain')]
    #countriesComparisonTables = OnDataProcessing.compareCountryTables(['united-kingdom', 'italy'])
    displayData.runServer(app, startingCountry, combinedCountries)#, countriesComparisonTables)

    return app


if __name__ == '__main__':
    app = main()
    app.run_server(debug=True)
