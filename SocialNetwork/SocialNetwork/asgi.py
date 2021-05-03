"""
ASGI config for SocialNetwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
import Chats.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialNetwork.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Chats.routing.websocket_urlpatterns
        )
    ),
})