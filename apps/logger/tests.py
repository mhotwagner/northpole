from django.test import TestCase

# Create your tests here.
class LoggerTests(TestCase):
    def test_a_log_can_be_posted(self):

        self.assertEqual(Log.objects.count(), 0)

        self.client.post(
            '/api/logs',
            {'message': 'Some test message'},
        )

        Log.objects.get
