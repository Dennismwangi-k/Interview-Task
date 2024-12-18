from rest_framework.test import APITestCase
from rest_framework import status
from .models import ClosestPoints

class ClosestPointsViewTestCase(APITestCase):
    def test_closest_points_post(self):
        data = {"points_string": "(2,3), (1,1), (5,4)"}
        response = self.client.post('/api/points/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('closest_pair', response.data)

    def test_closest_points_get(self):
        response = self.client.get('/api/points/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
