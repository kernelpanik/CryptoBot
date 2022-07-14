import requests
from binance import ThreadedWebsocketManager
import os
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
from binance import AsyncClient, BinanceSocketManager
from binance.enums import *





# channel_layer = get_channel_layer()

# def get_crypto_info ():
#     price = "15000000"
#     async_to_sync(channel_layer.group_send)(
#             "crypto_ohlcv", {"type": "get.price",
#                        "event": "New Price",
#                        "text": price})

api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")


# def websocket_kline(slug):
#     symbol = slug
#     twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
#     # start is required to initialise its internal loop
#     twm.start()
#     def handle_socket_message(msg):
#         print(f"message type: {msg['e']}")
#         print(msg)
#     twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)
 
#     # # multiple sockets can be started
#     # twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)
#     # twm.start_symbol_ticker_socket(callback=handle_socket_message, symbol=symbol)


#     # # or a multiplex socket can be started like this
#     # # see Binance docs for stream names
#     # streams = ['bnbusdt@ticker']
#     # twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

#     twm.join()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(websocket_kline(slug))





async def websocket_kline(slug):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.kline_socket('BNBBTC', interval=KLINE_INTERVAL_30MINUTE)
    print(ts)
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)


  