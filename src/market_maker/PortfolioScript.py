def get_portfolio(self):
    contracts = settings.CONTRACTS
    portfolio = {}
    for symbol in contracts:
        position = self.bitmex.position(symbol=symbol)
        instrument = self.bitmex.instrument(symbol=symbol)

        if instrument['isQuanto']:
            future_type = "Quanto"
        elif instrument['isInverse']:
            future_type = "Inverse"
        elif not instrument['isQuanto'] and not instrument['isInverse']:
            future_type = "Linear"
        else:
            raise NotImplementedError("Unknown future type; not quanto or inverse: %s" % instrument['symbol'])

        if instrument['underlyingToSettleMultiplier'] is None:
            multiplier = float(instrument['multiplier']) / float(instrument['quoteToSettleMultiplier'])
        else:
            multiplier = float(instrument['multiplier']) / float(instrument['underlyingToSettleMultiplier'])

        portfolio[symbol] = {
            "currentQty": float(position['currentQty']),
            "futureType": future_type,
            "multiplier": multiplier,
            "markPrice": float(instrument['markPrice']),
            "spot": float(instrument['indicativeSettlePrice'])
        }

    return portfolio


