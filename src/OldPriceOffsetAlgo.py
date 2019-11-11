delta = self.exchange.calc_delta()['spot']

        ticker = self.exchange.bitmex.ticker_data()
        tickLog = self.exchange.get_instrument()['tickLog']
        position = self.exchange.get_position()

        currentQty = self.exchange.get_delta()
            #newTime = time.time()

        priceChange = self.priceChange()

        if float(currentQty) > 0 and ticker["sell"] < float(position['avgEntryPrice']):

            self.start_position_buy =  ticker["buy"] - 8 * self.instrument['tickSize'] #((position['avgEntryPrice']) - priceChange) #- self.pricechange)  *2) /2  - 3 * self.instrument['tickSize'] #self.start_position_buy =  ticker["buy"] + self.instrument['tickSize'] #floatposiitonworks. hoorah!
            self.start_position_sell = position['avgEntryPrice'] + 2 * self.instrument['tickSize']


        if float(currentQty) < 0 and ticker["buy"] > float(position['avgEntryPrice']):

            self.start_position_sell = ticker["sell"] + 8 * self.instrument['tickSize'] #((position['avgEntryPrice']) + priceChange) # + self.pricechange)  *2) /2 + 3 * self.instrument['tickSize']  # self.start_position_sell = ticker["sell"] - self.instrument['tickSize'] #ticker["sell"] - self.instrument['tickSize']
            self.start_position_buy = position['avgEntryPrice'] - 2 * self.instrument['tickSize']


        else:
            self.start_position_buy = ticker["buy"]
            self.start_position_sell = ticker["sell"]


        if index == 1:

            if self.start_position_sell > ticker["sell"]:

                return round(self.start_position_sell *2) /2

            else:
                return round((ticker["sell"]) + 4 * self.instrument['tickSize'], 2)
    #this bit is going wrong atm. getting rounding wrong is difficult.fixed.


        if index == 2:
            while priceChange < 20:
                return round(self.start_position_sell) + 25

            else:
                return round((position['avgEntryPrice'] + priceChange) *2) /2

        if index == -1:

            if self.start_position_buy < ticker["buy"]:

                return round(self.start_position_buy *2) /2

            else:
                return round(ticker["buy"] - 4 * self.instrument['tickSize'], 2)

        if index == -2:
            while priceChange < 20:
                return round(self.start_position_buy) - 25

            else:
                return round((position['avgEntryPrice'] - priceChange) *2) /2

            #need to fix this for getting out of orders, so that it reverts quicker.

        else:
            return math.toNearest(round(self.exchange.get_instrument()['midPrice']) * (1 + settings.INTERVAL) ** index, self.instrument['tickSize'])
