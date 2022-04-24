from typing import Any
from binance.client import Client
import pandas as pd
from binance.exceptions import BinanceAPIException
import requests
import json
import hashlib
from urllib.parse import urlencode
import hmac
from ..models import CoinList, BinanceSymbolList
import os

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
