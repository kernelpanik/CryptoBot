"""
ASGI config for website project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

# more import from consumers
# from chat.consumers import AdminChatConsumer, PublicChatConsumer


application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
            # url(r"^chat/$", PublicChatConsumer.as_asgi()),
        ])
    ),
})




# old
# application = get_asgi_application()
# application = AmazingMiddleware(application)
