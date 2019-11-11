from market_maker.market_maker import OrderManager

class CustomOrderManager(OrderManager):
    def place_orders(self) -> None:
        # implement your custom strategy here
        buy_orders = []

        buy_orders.append({'price': 998.0, 'orderQty': 100, 'side': "Buy"})
        buy_orders.append({'price': 999.0, 'orderQty': 100, 'side': "Buy"})

order_manager = CustomOrderManager()

def run() -> None:
    order_manager = CustomOrderManager()

    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        order_manager.run_loop()
    except (KeyboardInterrupt):
        sys.exit()
