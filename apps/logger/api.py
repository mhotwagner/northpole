from django.conf import settings
from rest_framework import viewsets, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

import logging

from .models import Log
from ..ornaments.models import OrnamentDevice

logger = logging.getLogger(__name__)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['ornament', 'message']


class LogViewSet(viewsets.GenericViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    @staticmethod
    def _get_log_data(raw_data: dict):
        ornament_key = 'ornament_mac_address' if 'ornament_mac_address' in raw_data.keys() else 'ornament_id'
        ornament_mac_address = raw_data[ornament_key].replace(':', '')
        ornament = get_object_or_404(OrnamentDevice.objects.all(),
                                     mac_address=ornament_mac_address)
        return {
            'message': raw_data['message'],
            'ornament': ornament.id,
        }

    def create(self, request):
        serializer = self.serializer_class(data=self._get_log_data(request.data))
        if serializer.is_valid():
            log = serializer.save()
            with open(settings.LOGGER_FILE_PATH, 'a+') as logfile:
                logfile.write("\n" + request.data['message'])
            return Response({'id': log.id})
        return Response({'message': 'Bad data', 'errors': serializer.errors}, status=400)
