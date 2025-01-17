from common.factories.twenty_four_seven.tfs_item import ItemFactory
from rest_framework.test import APITestCase
from rest_framework import status
import json


class AISummaryTests(APITestCase):
    def test_ai_summary_endpoint(self):
        item = ItemFactory(text='New text')
        response = self.client.get(f'/api/twenty_four_seven/summary/{item.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertIsNotNone(content['summary'])
        self.assertIsNotNone(content['summary_ar'])
