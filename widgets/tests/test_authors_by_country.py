from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AuthorsByCountryTests(APITestCase):
  def test_authors_by_country(self):
    flink1 = FeedlinksFactory(source1='one_source', country='England')
    flink2 = FeedlinksFactory(source1='two_source', country='USA')
    flink3 = FeedlinksFactory(source1='third_source', country='Greece')
    PostFactory(feedlink=flink1, entry_author='AFP')
    PostFactory(feedlink=flink2, entry_author='EFP')
    PostFactory(feedlink=flink2, entry_author='EFP')
    PostFactory(feedlink=flink3, entry_author='CFP')
    PostFactory(feedlink=flink3, entry_author='CFP')
    PostFactory(feedlink=flink3, entry_author='CFE')
    PostFactory(feedlink=flink3, entry_author='CFE')

    pr = ProjectFactory()
    widget_pk = pr.widgets_list_2.authors_by_country_id
    url = reverse('widgets:onl_authors_by_country', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'Greece': {'CFE': 2, 'CFP': 2}}, 
            {'USA': {'EFP': 2}}, 
            {'England': {'AFP': 1}}
          ]
    self.assertEqual(json.loads(response.content), res)
