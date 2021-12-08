import ccxt
import pandas as pd
from ccxt import binanceus
from datetime import datetime

"""
Will transform into a class for backtesting
"""


def fetch_historical_data(exchange: str, target: str, fiat: str):
    if exchange == 'binanceus':
        exchange = binanceus()

        trading_pair = target + '/' + fiat
        data = exchange.fetch_ohlcv(trading_pair, '1h')

        dates = []
        open_data = []
        high_data = []
        low_data = []
        close_data = []

        # for candle in candles:
        #     dates.append(datetime.fromtimestamp(candle[0] / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f'))
        #     open_data.append(candle[1])
        #     high_data.append(candle[2])
        #     low_data.append(candle[3])
        #     close_data.append(candle[4])

        # Get data
        header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = pd.DataFrame(data, columns=header).set_index('Timestamp')
        # Save it
        print(f"Downloaded {trading_pair} - 1h")
        filename = './data/historical_data/{}-{}-{}.csv'.format(
            exchange, target, "1h")
        df.to_csv(filename)
