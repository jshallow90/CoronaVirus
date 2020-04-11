import OnDataProcessing
import displayData
import machineLearning
from IPython.display import display, HTML


def main():
    countryList = ['united-states', 'italy', 'united-kingdom', 'france', 'germany', 'spain', 'china']
    displayData.compareCounties(countryList, 'deaths')
    machineLearning.getCountryData('united-kingdom')


if __name__ == '__main__':
    main()
