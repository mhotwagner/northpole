from django.test import TestCase


class TestStatus(TestCase):
    def test_the_route_returns_a_200(self):
        response = self.client.get('/api/status/')
        self.assertEqual(response.status_code, 200)
