from django.urls import path, include
from rest_framework import routers

from .api import OrnamentViewSet

router = routers.DefaultRouter()

router.register('ornaments', OrnamentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
