from django.conf import settings
from django.http import Http404
from rest_framework import viewsets, serializers
from rest_framework.response import Response

import logging

from .models import Log

logger = logging.getLogger(__name__)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class LogViewSet(viewsets.GenericViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def create(self, request):
        message = request.data['message']
        log = self.queryset.create(message=message)
        with open(settings.LOGGER_FILE_PATH, 'a+') as logfile:
            logfile.write("\n" + message)
        return Response({'id': log.id})
