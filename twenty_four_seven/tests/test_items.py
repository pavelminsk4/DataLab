from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.twenty_four_seven.tfs_project import ProjectTwentyFourSevenFactory
from common.factories.twenty_four_seven.tfs_item import ItemFactory


class ItemTests(APITestCase):
    def test_item_endpoint(self):
        project = ProjectTwentyFourSevenFactory()
        item = ItemFactory(project=project)
        url = reverse('twenty_four_seven:project-items-detail',
                      args=(project.pk, item.pk))
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content)['is_back'], False)
        self.assertEqual(json.loads(response.content)['status'], 'PCK')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {
            'is_back': True,
            'status': 'IRR',
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['is_back'], True)
        self.assertEqual(json.loads(response.content)['status'], 'IRR')
