from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopCountriesTests(APITestCase):
    def test_response_list(self):
        flink1 = FeedlinksFactory(country='England')
        flink2 = FeedlinksFactory(country='USA')
        flink3 = FeedlinksFactory(country='Canada')
        PostFactory.create_batch(2, feedlink=flink1)
        PostFactory.create_batch(4, feedlink=flink2)
        PostFactory.create_batch(2, feedlink=flink3)
        pr = ProjectFactory()

        widget_pk = pr.widgets_list_2.top_countries_id
        url = reverse('widgets:onl_top_countries', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'feedlink__country': 'USA', 'country_count': 4},
            {'feedlink__country': 'Canada', 'country_count': 2},
            {'feedlink__country': 'England', 'country_count': 2},
        ]
        self.assertEqual(json.loads(response.content), res)
