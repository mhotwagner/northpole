from django.urls import path

from .views import device_view, controller_view


urlpatterns = [
    path('ornaments/controller/<str:mac_address>/', controller_view),
    path('ornaments/device/<str:mac_address>/', device_view),
]
