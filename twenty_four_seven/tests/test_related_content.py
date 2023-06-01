from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.twenty_four_seven.tfs_project import ProjectTwentyFourSevenFactory
from common.factories.twenty_four_seven.tfs_item import ItemFactory


class RelatedContentTests(APITestCase):
    def test_related_content_endpoint(self):
        project = ProjectTwentyFourSevenFactory()
        items = ItemFactory.create_batch(10, project=project)
        url = reverse('twenty_four_seven:tfs_related_content-list')
        url = f'{url}?item={items[0].pk}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
