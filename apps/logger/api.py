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
        fields = ['ornament_mac_address', 'message']


class LogViewSet(viewsets.GenericViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    @staticmethod
    def _get_log_data(raw_data: dict):
        if 'ornament_mac_address' in raw_data.keys():
            return {
                'message': raw_data['message'],
                'ornament_mac_address': raw_data['ornament_mac_address'].replace(':', '')
            }
        return {'message': raw_data['message']}

    def create(self, request):
        serializer = self.serializer_class(data=self._get_log_data(request.data))
        if serializer.is_valid():
            log = serializer.save()
            with open(settings.LOGGER_FILE_PATH, 'a+') as logfile:
                logfile.write("\n" + request.data['message'])
            return Response({'id': log.id})
        return Response({'message': 'Bad data'}, status=400)
