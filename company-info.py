import yfinance as yf

def compileCompanyInformation(tickerSymbol):
    tickerData = yf.Ticker(tickerSymbol)

    companyInformation = {
        'name': "Company name: "+tickerData.info['longName']+", "+tickerData.info['symbol'],
        'sector': "Sector: "+tickerData.info['sector'],
        'location': "Location: "+tickerData.info['city']+", "+tickerData.info['state']+", "+tickerData.info['country'],
        'website': "Website: "+tickerData.info['website']
    }

    return companyInformation

def printCompanyInformation(companyInformation):
    for x in companyInformation:
        print(companyInformation[x])