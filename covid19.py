import OnDataProcessing
import displayData
import machineLearning


def main():
    #countryList = ['united-states', 'italy', 'united-kingdom', 'france', 'germany', 'spain', 'china']
    #displayData.compareCounties(countryList, 'deaths')
    displayData.showTable(OnDataProcessing.getCountryData('italy'))


if __name__ == '__main__':
    main()
