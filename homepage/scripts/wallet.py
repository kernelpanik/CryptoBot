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

# get Binance spot
def get_wallet_assets(info):
    own_btc_list = []
    own_usdt_list = []
    df = pd.DataFrame(info["balances"])
    df["free"] = df["free"].astype(float).round(4)
    df_assets = df[df["free"] > 0]
    pd.options.display.float_format = '{:.4f}'.format
    df_assets = df_assets.sort_values('asset')
    sum_usdt = 0.0
    current_btc_price_USD = client.get_symbol_ticker(symbol="BTCUSDT")["price"]
    for asset in df_assets['asset']:
        df = df_assets.loc[df_assets['asset'] == asset]
        asset_quantity = float(df["free"]) + float(df["locked"])  
        if asset == "BTC":
            sum_usdt += asset_quantity * float(current_btc_price_USD)
            btc_value = asset_quantity * float(current_btc_price_USD)
            own_btc_list.append(btc_value)
        else:
            btc_value = 0.0
            own_btc_list.append(btc_value)
            try:
                _price = client.get_symbol_ticker(symbol=asset + "USDT")
                sum_usdt += asset_quantity * float(_price["price"])
                usdt_value =  asset_quantity * float(_price["price"])
                own_usdt_list.append(usdt_value)
            except BinanceAPIException:
                usdt_value = 0.0
                own_usdt_list.append(usdt_value)
                continue
    spot_btc = sum_usdt / float(current_btc_price_USD)
    spot_usdt = sum_usdt
    df_assets['ownusdt'] = own_usdt_list
    df_assets['ownbtc'] = own_btc_list
    return df_assets, spot_usdt, spot_btc

# Get Binance savings
def get_binance_savings():
    servertime = requests.get("https://api.binance.com/api/v1/time")
    servertimeobject = json.loads(servertime.text)
    servertimeint = servertimeobject['serverTime']
    params = urlencode({
        "timestamp" : servertimeint,
    })
    hashedsig = hmac.new(api_secret.encode('utf-8'), params.encode('utf-8'),hashlib.sha256).hexdigest()
    save_balance = requests.get("https://api.binance.com/sapi/v1/lending/union/account",
    params = {
        "timestamp" : servertimeint,
        "signature" : hashedsig,   
    },
    headers = {
        "X-MBX-APIKEY" : api_key,
    }
    )
    save_balance = save_balance.text
    save_balance = json.loads(save_balance)
    return save_balance

# Get Binance stake

