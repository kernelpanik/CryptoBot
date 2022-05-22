from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application


application = ProtocolTypeRouter({
    # (your routes here)
     "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})