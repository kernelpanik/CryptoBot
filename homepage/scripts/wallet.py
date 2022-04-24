from typing import Any
from binance.client import Client
import pandas as pd
from binance.exceptions import BinanceAPIException
import requests
import json
import hashlib
from urllib.parse import urlencode
import hmac
from ..models import CoinList, BinanceSymbolList, WalletAssetList
import os

api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")

# initialize
client = Client(api_key, api_secret)

# get account info
info = client.get_account()


# get all crpyto in wallet, sarebbe da suddividere tra spot e stacking
def get_wallet_assets(info):
    df = pd.DataFrame(info["balances"])
    df["free"] = df["free"].astype(float).round(4)
    df_assets = df[df["free"] > 0]
    pd.options.display.float_format = '{:.4f}'.format
    df_assets = df_assets.sort_values('asset')
    return df_assets


# df_assets = get_wallet_assets(info)

def get_spot_balance(info, df_assets):
        sum_usdt = 0.0
        current_btc_price_USD = client.get_symbol_ticker(symbol="BTCUSDT")["price"]
        for asset in df_assets['asset']:
            df = df_assets.loc[df_assets['asset'] == asset]
            asset_quantity = float(df["free"]) + float(df["locked"])  
            if asset == "BTC":
                sum_usdt += asset_quantity * float(current_btc_price_USD) 
            else:
                try:
                    _price = client.get_symbol_ticker(symbol=asset + "USDT")
                    sum_usdt += asset_quantity * float(_price["price"])
                except BinanceAPIException:
                    continue
#                    print("Coppia di crypto non trovata")
        own_btc = sum_usdt / float(current_btc_price_USD)
        own_usdt = sum_usdt
#        print(" * Spot => %.4f USDT == " % sum_usdt, end="")
#        print("%.8f BTC" % own_btc)
        #return own_usdt, own_btc
        return own_usdt







