from django.urls import path, include

from .views import test_view


urlpatterns = [
    path('ornaments/controller/<str:mac_address>/', test_view),
    path('ornaments/device/<str:mac_address>/', test_view),
]
