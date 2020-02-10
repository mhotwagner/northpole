from django.urls import path

from .views import device_view, controller_view, controller_nickname_view


urlpatterns = [
    path('o/<str:nickname>/', controller_nickname_view),
    path('ornaments/controller/<str:mac_address>/', controller_view),
    path('ornaments/device/<str:mac_address>/', device_view),
]
