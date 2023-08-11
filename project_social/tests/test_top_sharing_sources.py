from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopSharingSources(APITestCase):
    def test_sharing_sources_api(self):
        TweetBinderPostFactory(count_totalretweets='1', count_favorites='1', user_alias='@first', sentiment='neutral')
        TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', user_alias='@first', sentiment='positive')
        pr = ProjectSocialFactory()

        widget_pk = pr.social_widgets_list.top_sharing_sources_id
        url = reverse('project_social:social_top_sharing_sources', kwargs={'pk': pr.pk, 'widget_pk': widget_pk},)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'type': 'Most active author',
                'name': 'First_name',
                'alias': '@first',
                'value': 2,
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 1},
                'picture': None,
                'gender': 'male',
                'source': 'Twitter',
            },
            {
                'type': 'Most influential author',
                'name': 'First_name',
                'alias': '@first',
                'value': 6,
                'sentiments': {'positive': 1, 'negative': 0, 'neutral': 1},
                'picture': None,
                'gender': 'male',
                'source': 'Twitter',
            },
        ]
        self.assertEqual(json.loads(response.content), res)
