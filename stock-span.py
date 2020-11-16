import yfinance as yf

# Initialization of variables
nextTickerBool = True
global tickerString
global tickerPeriodStart
global tickerPeriodEnd


# Calculates the span from the specified start date to the specified end date
def calculateSpan(data):
    stockSpan = []
    stack = []
    prices = []

    for price in data:
        prices.append(price)

    stockSpan.append(1)
    stack.append(0)

    for i in range(1, len(prices)):
        while prices[i] > prices[stack[-1]]:
            stack.pop()

            if len(stack) == 0:
                break

        if len(stack) > 0:
            stockSpan.append(i-stack[-1])
        else:
            stockSpan.append(i+1)

        stack.append(i)

    return stockSpan


# Allows the user to input data they wish to find the span for
while nextTickerBool:
    tickerString = str(input("Ticker: ").strip().upper())
    tickerPeriodStart = str(input("\nStart date (Format YYYY-MM-DD): ").strip())
    tickerPeriodEnd = str(input("End date (Format YYYY-MM-DD): ").strip())

    ticker = yf.Ticker(tickerString)
    tickerHistory = ticker.history(period="1d", start=tickerPeriodStart, end=tickerPeriodEnd)

    print(calculateSpan(tickerHistory.Close))

    nextTicker = str(input("Next ticker?\nY or N: ").strip().upper())
    if nextTicker == 'Y':
        nextTickerBool = True
    else:
        nextTickerBool = False

print("Closing stock span.")




