from django.urls import re_path
from website.consumers import OhlcvConsumer



# channel_routing = [
#     re_path('websocket.connect', ws_connect),
#     re_path('websocket.disconnect', ws_disconnect),
# ]



websocket_urlpatterns = [
    # re_path(r"^(ws/ohlcv/price/)", OhlcvConsumer.as_asgi()),
    # re_path(r"^dashboard/(?P<stream>\w+)/$", OhlcvConsumer.as_asgi()),
    re_path(r"dashboard/ADAUSDT/ohlcv", OhlcvConsumer.as_asgi()),
]