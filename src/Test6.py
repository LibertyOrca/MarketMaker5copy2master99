import sys

from market_maker.market_maker import OrderManager

def run():

    om = OrderManager()
    # Try/except just keeps ctrl-c from printing an ugly stacktrace
    try:
        om.run_loop()
    except (KeyboardInterrupt):
        sys.exit()

while True:
    run()
