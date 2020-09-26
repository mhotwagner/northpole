from django.urls import path, include
from rest_framework import routers

from .api import LogViewSet

router = routers.DefaultRouter()

router.register('logs', LogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
