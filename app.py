from dash import Dash
from models.country import Country
from common import constants
from models.server import Server


def main():
    app = Dash(__name__, external_stylesheets=constants.external_stylesheets)

    startingCountry = Country('united-kingdom')
    combinedCountries = [Country('italy'), Country('spain')]
    #countriesComparisonTables = OnDataProcessing.compareCountryTables(['united-kingdom', 'italy'])
    Server.runServer(app=app, country=startingCountry, countries=combinedCountries)

    return app


if __name__ == '__main__':
    app = main()
    app.run_server(debug=True)
