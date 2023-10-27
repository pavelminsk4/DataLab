from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AuthorsByCountryTests(APITestCase):
    def test_authors_by_country(self):
        flink1 = FeedlinkFactory(country='England')
        flink2 = FeedlinkFactory(country='USA')
        flink3 = FeedlinkFactory(country='Greece')
        p1 = PostFactory(feedlink=flink1, entry_author='AFP')
        p2 = PostFactory(feedlink=flink2, entry_author='EFP', entry_title='1')
        p3 = PostFactory(feedlink=flink2, entry_author='EFP', entry_title='2')
        p4 = PostFactory(feedlink=flink3, entry_author='CFP', entry_title='1')
        p5 = PostFactory(feedlink=flink3, entry_author='CFP', entry_title='2')
        p6 = PostFactory(feedlink=flink3, entry_author='CFE')
        pr = ProjectFactory()

        for post in (p1, p2, p3, p4, p5, p6):
            pr.posts.add(post)

        widget_pk = pr.widgets_list_2.authors_by_country_id
        url = reverse('widgets:onl_authors_by_country', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        res = [
            {'Greece': [['CFP', 2], ['CFE', 1]]},
            {'England': [['AFP', 1]]},
            {'USA': [['EFP', 2]]}
        ]
        self.assertEqual(json.loads(response.content), res)
