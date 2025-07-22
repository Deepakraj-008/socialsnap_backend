import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat_messages.routing  # Assuming you have routing.py in messages app for WebSockets

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialsnap.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            messages.routing.websocket_urlpatterns
        )
    ),
})

