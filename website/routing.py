from django.urls import re_path

# from . import consumers
# from consumers import OhlcvConsumer
from website.consumers import OhlcvConsumer


websocket_urlpatterns = [
    # re_path(r"^(ws/ohlcv/price/)", OhlcvConsumer.as_asgi()),
    re_path(r"^dashboard/(?P<stream>\w+)/$", OhlcvConsumer.as_asgi()),
]