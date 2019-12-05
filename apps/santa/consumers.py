# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json


import logging
logger = logging.getLogger(__name__)


class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data_json = json.loads(text_data)
        data = data_json['data']

        logger.info(f'[INFO] RECEIVED DATA <{data}>')

        self.send(text_data=json.dumps({'data': data}))
