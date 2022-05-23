from django.urls import re_path

# from . import consumers
# from consumers import OhlcvConsumer
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/ohlcv/', consumers.OhlcvConsumer.as_asgi()),
]