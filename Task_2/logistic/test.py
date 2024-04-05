from unittest import TestCase

from rest_framework.test import APIClient


class Test(TestCase):
    def test_sample_view(self):
        client = APIClient()
        response = client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
