from django.urls import re_path

# from . import consumers
from consumers import OhlcvConsumer

websocket_urlpatterns = [
    re_path(r'ws/ohlcv/$', OhlcvConsumer.as_asgi()),
]