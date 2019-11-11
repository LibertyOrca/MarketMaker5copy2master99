




if instrumentChoice == "XBTH20":
    if currentQty < abs(self.exchange.get_delta["XBTUSD"]):
        self.start_position_buy = ticker["buy"]
        self.start_position_sell = float(position['avgEntryPrice'])

    if currentQty > abs(self.exchange.get_delta["XBTUSD"]):
        self.start_position_sell = ticker["sell"]
        self.start_position_buy = ticker["buy"] - 42

if instrumentChoice == "XBTUSD":
    if float(position['avgEntryPrice']) < ticker["buy"]:
        self.start_position_buy = float(position['avgEntryPrice'])
        self.start_position_sell = ticker["sell"]
    
    else:
        self.start_position_buy = ticker["buy"]
        self.start_position_sell = ticker["sell"] + 42
        

if currentQty > 0:

    if abs(currentQty) < abs(self.exchange.get_delta('XBTUSD')):
        self.start_position_sell = ticker["sell"]
        self.start_position_buy = ticker["buy"] - 30
    else:
        if float(position['avgEntryPrice']) > ticker["sell"]:
            self.start_position_sell = float(position['avgEntryPrice'])
            self.start_position_buy = ticker["buy"]
        else:
            self.start_position_sell = ticker["sell"]

            self.start_position_buy = ticker["buy"]
# + self.instrument['tickSize']  # self.start_position_sell = ticker["sell"] - self.instrument['tickSize'] #ticker["sell"] - self.instrument['tickSize']

if currentQty != abs(self.exchange.get_delta('XBTUSD')):
    # may want to change this vehaviour so it stops accumulating sells. up to you.

    if instrumentChoice == "XBTH20":
        self.start_position_buy = ticker["buy"]
        self.start_position_sell = ticker["sell"] + 30

    else:

        if float(position['avgEntryPrice']) < ticker["buy"]:

            self.start_position_buy = float(position['avgEntryPrice'])
            self.start_position_sell = ticker["sell"]


        else:
            self.start_position_buy = ticker["buy"]
            self.start_position_sell = ticker["sell"] + 30

if currentQty == 0:

    if instrumentChoice == "XBTUSD":
        self.start_position_sell = ticker["sell"]
        self.start_position_buy = ticker["buy"] - 50

    if instrumentChoice == "XBTH20":
        self.start_position_sell = ticker["sell"] + 50
        self.start_position_buy = ticker["buy"]

if index == 1:
    # these should be fine as long as order size is tiny if we're profitable.

    return round(self.start_position_sell * 2) / 2

if index == -1:
    return round(self.start_position_buy * 2) / 2

if instrumentChoice == 'XBTH20':
    if self.exchange.get_delta('XBTUSD') == 0:
        if index == 1:
            quantity = quantity

    else:
        if currentQty > abs(self.exchange.get_delta('XBTUSD')):
            quantity = quantity

        else:
            if index == -1:
                quantity = quantity  # abs(currentQty + self.exchange.get_delta('XBTUSD'))
            if index == 1:
                quantity = quantity

else:
    if currentQty < 0:

        if index == -1:
            if float(position['avgEntryPrice']) < ticker["buy"]:
                quantity = quantity

        if index == 1:
            quantity = quantity  # abs(quantity * math.exp(0.0005 * currentQty))
        else:
            if index == -1:
                quantity = quantity










portfolio[symbol] = {
                "currentQty": float(position['currentQty']),
                "futureType": future_type,
                "multiplier": multiplier,
                "markPrice": float(instrument['markPrice']),
                "spot": float(instrument['indicativeSettlePrice'])
            }
























