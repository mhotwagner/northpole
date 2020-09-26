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
        log = self.queryset.create(message=request.data['message'])
        return Response({'id': log.id})

    # def get_or_create_object(self):
    #     mac_address = self.kwargs['pk'].replace(':', '')
    #     return self.get_queryset().get_or_create(mac_address=mac_address)

    # def retrieve(self, request, *args, **kwargs):
    #     mac_address = self.kwargs['pk']
    #     if len(mac_address) != 17:
    #         raise Http404(f'{mac_address} is not a valid ornament identifier')
    #
    #     instance, created = self.get_or_create_object()
    #     if created:
    #         logger.info(f'[INFO] Created {instance}')
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data,
    #                     status=201 if created else 200)
