from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from apps.ornaments.routing import websocket_urlpatterns as ornament_websocket_urlpatterns
from apps.santa.routing import websocket_urlpatterns as santa_websocket_urlpatterns

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(santa_websocket_urlpatterns + ornament_websocket_urlpatterns),
    ),
})
