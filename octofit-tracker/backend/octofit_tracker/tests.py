from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, CustomUser, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Add similar tests for other models as needed
