from django.urls import path

from .consumers import OrnamentDeviceConsumer, OrnamentControllerConsumer

websocket_urlpatterns = [
    path(r'ws/ornaments/controller/<str:mac_address>/', OrnamentControllerConsumer),
    path(r'ws/ornaments/device/<str:mac_address>/', OrnamentDeviceConsumer),
]
