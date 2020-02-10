from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

import logging

from apps.ornaments.models import OrnamentDevice

logger = logging.getLogger(__name__)


class OrnamentConsumer(WebsocketConsumer):
    """Generic consumer for use in ornament handling"""
    @property
    def mac_address(self):
        return self.scope['url_route']['kwargs']['mac_address'].replace(':', '')

    @property
    def ornament(self):
        return OrnamentDevice.objects.get(mac_address=self.mac_address)


class OrnamentDeviceConsumer(OrnamentConsumer):
    """Consumer that will handle data communication with devices (ornaments)"""
    def connect(self):
        logger.info(f'[INFO] Received connection request from {self.ornament}')
        async_to_sync(self.channel_layer.group_add)(
            self.mac_address,
            self.channel_name,
        )
        self.accept()
        logger.info(f'[INFO] Connected to {self.ornament}')

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.mac_address,
            self.channel_name
        )
        logger.info(f'[INFO] Disconnected from {self.ornament}')

    # Receive message from WebSocket
    def receive(self, text_data):
        data_json = json.loads(text_data)
        data = data_json['data']

        logger.info(f'[INFO] Data received from {self.ornament}')
        logger.info(f'[INFO] {data}')

        async_to_sync(self.channel_layer.group_send)(
            self.mac_address,
            {
                'type': 'data',
                'data': data,
            }
        )

    # Receive message from room group
    def data(self, event):
        logger.info(f'[INFO] Data received from group {self.mac_address} by {self.ornament}')
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'data': data
        }))


class OrnamentControllerConsumer(OrnamentConsumer):
    """Consumer that will handle data communication with the controlers (apps, websites, etc)"""
    def connect(self):
        logger.info(f'[INFO] Received connection request from {self.ornament} controller')
        async_to_sync(self.channel_layer.group_add)(
            self.mac_address,
            self.channel_name,
        )
        self.accept()
        logger.info(f'[INFO] Connected to {self.ornament} controller')

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.mac_address,
            self.channel_name
        )
        logger.info(f'[INFO] Disconnected from {self.ornament} controller')

    # Receive message from WebSocket
    def receive(self, text_data):
        data_json = json.loads(text_data)
        data = data_json['data']

        logger.info(f'[INFO] Data received from {self.ornament} controller')
        logger.info(f'[INFO] {data}')

        async_to_sync(self.channel_layer.group_send)(
            self.mac_address,
            {
                'type': 'data',
                'data': data,
            }
        )

    # Receive message from room group
    def data(self, event):
        logger.info(f'[INFO] Data received from group {self.mac_address} controller by {self.ornament}')
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'data': data
        }))