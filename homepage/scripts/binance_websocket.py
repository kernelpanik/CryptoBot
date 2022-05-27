import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()


def get_crypto_info ():
    price = "15000000"
    async_to_sync(channel_layer.group_send)(
            "crypto_ohlcv", {"type": "get.price",
                       "event": "New Price",
                       "text": price})

    