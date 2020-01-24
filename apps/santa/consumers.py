# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

import logging
logger = logging.getLogger(__name__)


class DataConsumer(WebsocketConsumer):
    def connect(self):
        logger.info('Attempting the socket connection!')
        self.group_name = 'ornaments'

        # Join group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data_json = json.loads(text_data)
        data = data_json['data']

        logger.info(f'[INFO] RECEIVED DATA <{data}>')

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'data',
                'data': data,
            }
        )

    # Receive message from room group
    def data(self, event):
        data = event['data']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'data': data
        }))
