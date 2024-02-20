import matplotlib.pyplot as plt

productAmount = 0

productCost = 316.30

moneyTrend = {}

weekCounter = 0

def calculateByEndWage(wage, percent): #How much money did you make for those 2 weeks?
    rawPercent = percent

    savingPercent = rawPercent / 100

    productPercent = ((100 - rawPercent) * .25 )/ 100

    leftProduct = ((100 - rawPercent) * .75 ) / 100

    savingMoney = (wage * savingPercent)

    productMoney = (wage * productPercent)

    leftoverMoney = (wage * leftProduct)

    global productAmount
    global productCost
    productAmount += productMoney

    productCost -= productMoney;

    global weekCounter
    weekCounter += 1

    moneyTrend[weekCounter] = wage

    print("Money Input")

    print("Money for savings rounded: $", round(savingMoney,2))

    print("Money for big purchase rounded: $", round(productMoney,2))

    print("Money left over rounded: $", round(leftoverMoney,2))

    print("Debt Remaining: $", round(productCost,2))

    print(moneyTrend)


def calculateMoneyByHour(hours):

    return hours * 15

def createGraph(moneyInfo):

    xValues = list(moneyInfo.keys())
    yValue = list(moneyInfo.values())

    plt.plot(xValues, yValue)

    plt.xlabel('Weeks')

    plt.ylabel('Taxed Money')

    plt.title('Money Trend')

    plt.show()


def main():

    calculateByEndWage(184.25, 20)

    calculateByEndWage(329.86, 20)

    createGraph(moneyTrend)

main()
