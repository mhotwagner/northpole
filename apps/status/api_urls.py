from django.urls import path

from apps.status.api import status_view

urlpatterns = [
    path('status/', status_view)
]
