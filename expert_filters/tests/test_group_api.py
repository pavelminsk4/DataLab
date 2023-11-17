from common.factories.expert_filters.preset import PresetFactory
from common.factories.expert_filters.group import GroupFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class GroupTests(APITestCase):
    def test_group_list(self):
        user = User.objects.create(username='MiskKSA')
        user2 = User.objects.create(username='Stranger')
        self.client.force_login(user2)

        ps1 = PresetFactory(
            title='First preset',
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

        g1 = GroupFactory(
            title='First Group',
            description='Very userful description',
            creator=user
        )

        g2 = GroupFactory(
            title='Second Group',
            description='Description than no one reads',
            creator=user2
        )

        g2.presets.add(ps3.id)

        url = reverse('expert_filters:groups-list')
        response = self.client.get(url)

        res = [
            {
                'id': g2.id,
                'title': 'Second Group',
                'description': 'Description than no one reads',
                'creator': user2.id,
                'updated_at': g2.updated_at.replace(tzinfo=None).isoformat() + 'Z',
                'created_at': g2.created_at.replace(tzinfo=None).isoformat() + 'Z',
                'presets': [
                    {
                        'id': ps3.id,
                        'title': 'Stranger preset',
                        'query': ['cat OR dog', 'red OR blue'],
                        'creator': user2.id,
                        'updated_at': ps3.updated_at.replace(tzinfo=None).isoformat() + 'Z',
                        'created_at': ps3.created_at.replace(tzinfo=None).isoformat() + 'Z',
                    }
                ]
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), res)
