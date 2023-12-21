from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json
from common.factories.twenty_four_seven.tfs_project import ProjectTwentyFourSevenFactory
from common.factories.twenty_four_seven.tfs_item import ItemFactory
from common.factories.post import PostFactory


def exclude(data, keys):
    return {k: v for k, v in data.items() if k not in keys}


class ItemTests(APITestCase):
    maxDiff = None

    def setUp(self):
        self.project = ProjectTwentyFourSevenFactory()
        self.post    = PostFactory()
        self.item    = ItemFactory(project=self.project, post=self.post)
        self.path    = f'/api/twenty_four_seven/projects/{self.project.id}/items/{self.item.id}/'

    def test_get_item_details(self):
        """GET 24/7 project item details should return the serialized item"""
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(exclude(json.loads(response.content), ['id', 'post']), {
            'header': 'Header Text',
            'header_ar': '',
            'in_work': False,
            'is_back': False,
            'linked_items': [],
            'original_content': None,
            'project': self.project.id,
            'social_post': None,
            'status': 'PCK',
            'text': 'Description Text',
            'text_ar': ''
        })

    def test_patch_item_details(self):
        """PATCH 24/7 project item details should update the item"""
        response = self.client.patch(self.path, {
            'header': 'New Header', 'text': 'New Text', 'header_ar': 'رأس جديد', 'text_ar': 'نص جديد'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(exclude(json.loads(response.content), ['id', 'post']), {
            'header': 'New Header',
            'header_ar': 'رأس جديد',
            'in_work': False,
            'is_back': False,
            'linked_items': [],
            'original_content': None,
            'project': self.project.id,
            'social_post': None,
            'status': 'PCK',
            'text': 'New Text',
            'text_ar': 'نص جديد'
        })
