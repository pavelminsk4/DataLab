from common.factories.expert_filters.preset import PresetFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class PresetTests(APITestCase):
    def test_preset_list(self):
        user = User.objects.create(username='MiskKSA')
        user2 = User.objects.create(username='Stranger')
        self.client.force_login(user)

        ps1 = PresetFactory(
            title='First preset',
            query=['lime AND salt'],
            creator=user
        )

        ps2 = PresetFactory(
            title='Second preset',
            creator=user 
        )

        ps3 = PresetFactory(
            title='Stranger preset',
            creator=user2
        )

        url = reverse('expert_filters:presets-list')
        response = self.client.get(url)


        res1 = {
            'id': ps1.id,
            'title': 'First preset',
            'query': ['lime AND salt'],
            'creator': user.id,
            'updated_at': ps1.updated_at.replace(tzinfo=None).isoformat() + 'Z',
            'created_at': ps1.created_at.replace(tzinfo=None).isoformat() + 'Z',
        }

        res2 = {
            'id': ps2.id,
            'title': 'Second preset',
            'query': ['cat OR dog', 'red OR blue'],
            'creator': user.id,
            'updated_at': ps2.updated_at.replace(tzinfo=None).isoformat() + 'Z',
            'created_at': ps2.created_at.replace(tzinfo=None).isoformat() + 'Z',
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [res1, res2])
