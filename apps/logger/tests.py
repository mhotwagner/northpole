import os
from datetime import datetime

from django.conf import settings
from django.test import TestCase

# Create your tests here.
from .api import LogSerializer, LogViewSet
from .models import Log


class LoggerTests(TestCase):
    def tearDown(self):
        if os.path.exists(settings.LOGGER_FILE_PATH):
            os.remove(settings.LOGGER_FILE_PATH)

    def test_a_log_can_be_posted(self):
        self.assertEqual(Log.objects.count(), 0)
        self.client.post('/api/logs/', {'message': 'Some test message'})
        self.assertEqual(Log.objects.count(), 1)
        self.assertEqual(
            Log.objects.first().message,
            'Some test message'
        )

    def test_it_writes_to_the_logfile(self):
        timestamp = datetime.now()
        self.client.post('/api/logs/', {'message': str(timestamp)})
        with open(settings.LOGGER_FILE_PATH) as fp:
            self.assertTrue(fp.read().endswith(str(timestamp)))

    def test_serializer_can_accept_data_object_and_create_instance(self):
        self.assertEqual(Log.objects.count(), 0)
        timestamp = datetime.now()
        data = {'message': str(timestamp), 'ornament_mac_address': 'ab:cd:ef:01:23'}
        serializer = LogSerializer(data=LogViewSet._get_log_data(data))
        serializer.is_valid()
        serializer.save()
        self.assertEqual(Log.objects.count(), 1)
        self.assertEqual(Log.objects.first().message, str(timestamp))
        self.assertEqual(Log.objects.first().ornament_mac_address, 'abcdef0123')
