import os
from datetime import datetime

from django.conf import settings
from django.test import TestCase

from .models import Log
from ..ornaments.models import OrnamentDevice


class LoggerTests(TestCase):
    def setUp(self):
        self.ornament = OrnamentDevice.objects.create(mac_address='01:23:45:67:89:ab')

    def tearDown(self):
        if os.path.exists(settings.LOGGER_FILE_PATH):
            os.remove(settings.LOGGER_FILE_PATH)

    def test_a_log_can_be_posted(self):
        self.assertEqual(Log.objects.count(), 0)
        self.client.post('/api/logs/', {'message': 'Some test message', 'ornament_id': self.ornament.mac_address})
        self.assertEqual(Log.objects.count(), 1)
        self.assertEqual(
            Log.objects.first().message,
            'Some test message'
        )

    def test_it_writes_to_the_logfile(self):
        timestamp = datetime.now()
        self.client.post('/api/logs/', {'message': str(timestamp), 'ornament_id': self.ornament.mac_address})
        with open(settings.LOGGER_FILE_PATH) as fp:
            self.assertTrue(fp.read().endswith(str(timestamp)))
