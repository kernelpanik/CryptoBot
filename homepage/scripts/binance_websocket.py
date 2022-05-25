import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()


def get_stock_info ():
    price = "150.34"
    async_to_sync(channel_layer.group_send)('crypto', {'type': 'send_info', 'text': price})

    