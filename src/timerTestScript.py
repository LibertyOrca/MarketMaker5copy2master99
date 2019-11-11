import time

originalTime = time.time()

originalentryprice = 50

def tradeStrat(originalTime):
    originalentryprice = 50
    newtime = time.time()


    pricechange = (newtime - originalTime) * (5/ 1440)


    priceMax = originalentryprice + pricechange
    priceMin = originalentryprice - pricechange
    print(priceMax)

tradeStrat(originalTime)
