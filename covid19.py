import OnDataProcessing


def main():
    countryList = ['united-states', 'italy', 'united-kingdom', 'france', 'germany', 'spain', 'china']
    for country in countryList:
        OnDataProcessing.combineCountryStatistics(country, True)
    # compareCounties(['us', 'italy', 'united-kingdom', 'france', 'germany', 'spain'], 'deaths', ignoreZeroDates=True)


if __name__ == '__main__':
    main()
