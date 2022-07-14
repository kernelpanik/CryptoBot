import requests
from binance import ThreadedWebsocketManager
import os
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# channel_layer = get_channel_layer()

# def get_crypto_info ():
#     price = "15000000"
#     async_to_sync(channel_layer.group_send)(
#             "crypto_ohlcv", {"type": "get.price",
#                        "event": "New Price",
#                        "text": price})

api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")


def websocket_kline():
    symbol = 'BNBUSDT'
    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()
    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)
 
    # # multiple sockets can be started
    # twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)
    # twm.start_symbol_ticker_socket(callback=handle_socket_message, symbol=symbol)


    # # or a multiplex socket can be started like this
    # # see Binance docs for stream names
    # streams = ['bnbusdt@ticker']
    # twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()

if __name__ == "__websocket_kline__":
   websocket_kline()



    