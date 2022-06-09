from typing import Any
from binance.client import Client
import pandas as pd
import datetime as dt
from binance.exceptions import BinanceAPIException
import requests
import json
import hashlib
from urllib.parse import urlencode
import hmac
from ..models import CoinList, BinanceSymbolList, Ohlcv
import os
from sqlalchemy import create_engine


api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

# initialize
client = Client(api_key, api_secret)


# Get all Binance symbols
def get_binance_symbol():
    symbol_list = []
    exchange_info = client.get_exchange_info()
    for n in exchange_info['symbols']:
        symbol = n['symbol']
        symbol_list.append(symbol)
    return symbol_list    




def get_old_ohlcv(slug):
    # obj = CoinList.objects.filter(coin=slug,price__isnull=True)
    # if obj.exists():
    #     past_days = 5
    #     status = True
    # else:
    #     past_days = 1
    #     status = False  

    past_days = 1
    client = Client()
    interval = '1h'
    start_str = str(
        (pd.to_datetime('today')-pd.Timedelta(str(past_days)+' days')).date())
    D = pd.DataFrame(client.get_historical_klines(
        symbol=slug, start_str=start_str, interval=interval))
    D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume',
                 'close_time', 'qav', 'num_trades', 'taker_base_vol',
                 'taker_quote_vol', 'is_best_match']
    D['date'] = [
        dt.datetime.fromtimestamp(x/1000) for x in D.open_time]
    dfohlcv = D[['date', 'open', 'high', 'low', 'close',
                 'volume', 'num_trades', 'taker_base_vol', 'taker_quote_vol']]
    print(dfohlcv)
    engine = create_engine('sqlite:///db.sqlite3', echo=False)
    dfohlcv.to_sql(Ohlcv._meta.db_table,
                           if_exists='append', con=engine, index=False)    


    # Ohlcv.objects.update_or_create( \
    #             defaults={'free': free, 'locked': locked, \
    #             'ownusdt': ownusdt, 'ownbtc': ownbtc}, \
    #             asset=asset )                       

    return True, dfohlcv