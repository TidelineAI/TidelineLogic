from Contexts.Context import Context
import alpaca_trade_api as tradeapi


# class to implement Context methods that execute in a backtesting environment

# TODO: Set up a mock api with same methods as trade api
# TODO: Get prices using paper trading api

class Backtest(Context):

    def __init__(self):
        super().__init__()

    def buy(self, ticker, order_type, units, limit_price=None):
        return

    def sell(self, ticker, order_type, units, limit_price=None):
        return

    def get_api(self):
        return tradeapi.REST(
            key_id='PKIG33U7XYR8ECVMMF4A',
            secret_key='e83t4Cn5oY07EENvlhRKwjKyTbykd8wn8Phesmze',
            base_url='https://paper-api.alpaca.markets')

    def get_barset(self, symbols, timeframe, limit, start, end):
        return self.get_api().get_barset(
            symbols,
            timeframe,
            limit=limit,
            start=start,
            end=end)

    def get_clock(self):
        return

    def get_account(self):
        return

    def list_positions(self):
        return
