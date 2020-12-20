"""northpole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.santa import urls as santa_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls, name='admin'),
    path('', include('apps.santa.urls'), name='santa'),
    path('', include('apps.ornaments.urls'), name='ornaments'),

    path('api/', include('apps.logger.api_urls'), name='logger_api'),
    path('api/', include('apps.ornaments.api_urls'), name='ornaments_api'),
    path('api/', include('apps.status.api_urls'), name='status_api'),
]
