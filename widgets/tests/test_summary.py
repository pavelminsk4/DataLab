from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from project.models import Post
import json


class SummaryTests(APITestCase):
    def test_response_list(self):
        p1 = PostFactory.create_batch(4, entry_author='AFP')
        p2 = PostFactory.create_batch(2, entry_author='EFE', sentiment='positive')
        pr = ProjectFactory()
        for p in p1:
            pr.posts.add(p)
        for p in p2:
            pr.posts.add(p)
        widget_pk = pr.widgets_list_2.summary_id
        url = reverse('widgets:onl_summary', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'posts': 6, 
            'sources': len(Post.objects.values('feedlink__source1').distinct()), 
            'authors': 2, 
            'countries': len(Post.objects.values('feedlink__country').distinct()), 
            'languages': len(Post.objects.values('feed_language_id').distinct()), 
            'positive': 2, 
            'negative': 0, 
            'neutral': 4, 
            'reach': 0
            }
        self.assertEqual(json.loads(response.content), res)
