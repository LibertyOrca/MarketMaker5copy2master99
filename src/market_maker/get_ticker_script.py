def get_ticker(self):
    ticker = self.exchange.get_ticker()
    tickLog = self.exchange.get_instrument()['tickLog']
    position = self.exchange.get_position()
    delta = self.exchange.calc_delta()['spot']
    # bestbuy = self.exchange.get_highest_buy()
    # bestsell = self.exchange.get_lowest_sell()

    # Set up our buy & sell positions as the smallest possible unit above and below the current spread
    # and we'll work out from there. That way we always have the best price but we don't kill wide
    # and potentially profitable spreads.

    # if i'm long - and the best sell price is less than the price i bought it at - buy at bid, sell at average entry.

    if float(delta) > 0 and ticker["sell"] < float(position['avgEntryPrice']):
        self.start_position_buy = ticker[
            "buy"]  # - self.instrument['tickSize']  # - self.instrument['tickSize'] #self.start_position_buy =  ticker["buy"] + self.instrument['tickSize'] #floatposiitonworks. hoorah!
        self.start_position_sell = round(position['avgEntryPrice'])

    if float(delta) < 0 and ticker["buy"] > float(position['avgEntryPrice']):
        self.start_position_sell = (ticker[
            "sell"])  # + self.instrument['tickSize'] #+ self.instrument['tickSize']  # self.start_position_sell = ticker["sell"] - self.instrument['tickSize'] #ticker["sell"] - self.instrument['tickSize']
        self.start_position_buy = round(position['avgEntryPrice'])

    else:
        self.start_position_sell = ticker["sell"]
        self.start_position_buy = ticker["buy"]

    # Midpoint, used for simpler order placement.
    self.start_position_mid = ticker["mid"]
    logger.info(
        "%s Ticker: Buy: %.*f, Sell: %.*f" %
        (self.instrument['symbol'], tickLog, ticker["buy"], tickLog, ticker["sell"])
    )
    logger.info('Start Positions: Buy: %.*f, Sell: %.*f, Mid: %.*f' %
                (tickLog, self.start_position_buy, tickLog, self.start_position_sell,
                 tickLog, self.start_position_mid))

    return ticker
