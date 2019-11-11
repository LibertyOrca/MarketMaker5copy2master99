tickLog = self.exchange.get_instrument()['tickLog']

to_amend = []
to_create = []
to_cancel = []
buys_matched = 0
sells_matched = 0
existing_orders = self.exchange.get_orders()

# Check all existing orders and match them up with what we want to place.
# If there's an open one, we might be able to amend it to fit what we want.

for order in existing_orders:
    try:
        if order['side'] == 'Buy':
            desired_order = buy_orders[buys_matched]
            buys_matched += 1
        else:
            desired_order = sell_orders[sells_matched]
            sells_matched += 1

        # Found an existing order. Do we need to amend it?
        if desired_order['orderQty'] != order['leavesQty'] or (
                # If price has changed, and the change is more than our RELIST_INTERVAL, amend.
                desired_order['price'] != order['price'] and
                abs((desired_order['price'] / order['price']) - 1) > settings.RELIST_INTERVAL):
            to_amend.append({'orderID': order['orderID'], 'orderQty': order['cumQty'] + desired_order['orderQty'],
                             'price': desired_order['price'], 'side': order['side']})
    except IndexError:
        # Will throw if there isn't a desired order to match. In that case, cancel it.
        to_cancel.append(order)

while buys_matched < len(buy_orders):
    to_create.append(buy_orders[buys_matched])
    buys_matched += 1

while sells_matched < len(sell_orders):
    to_create.append(sell_orders[sells_matched])
    sells_matched += 1

if len(to_create) > 0:
    logger.info("Creating %d orders:" % (len(to_create)))
    for order in reversed(to_create):
        logger.info("%4s %d @ %.*f" % (order['side'], order['orderQty'], tickLog, order['price']))
    self.exchange.create_bulk_orders(to_create)

# Could happen if we exceed a delta limit
if len(to_cancel) > 0:
    logger.info("Canceling %d orders:" % (len(to_cancel)))
    for order in reversed(to_cancel):
        logger.info("%4s %d @ %.*f" % (order['side'], order['leavesQty'], tickLog, order['price']))
    self.exchange.cancel_bulk_orders(to_cancel)