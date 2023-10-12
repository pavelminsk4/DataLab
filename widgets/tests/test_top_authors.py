from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopAuthorsTests(APITestCase):
    def test_response_list(self):
        p1 = PostFactory.create_batch(4, entry_author='AFP')
        p2 = PostFactory.create_batch(2, entry_author='EFE')
        pr = ProjectFactory()
        for p in p1:
            pr.posts.add(p)
        for p in p2:
            pr.posts.add(p)
        widget_pk = pr.widgets_list_2.top_authors_id
        url = reverse('widgets:onl_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'entry_author': 'AFP', 'author_posts_count': 4},
            {'entry_author': 'EFE', 'author_posts_count': 2},
        ]
        self.assertEqual(json.loads(response.content), res)
