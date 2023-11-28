from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class SummaryWidgetTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory(count_totalretweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', user_location='USA', sentiment='neutral')
        TweetBinderPostFactory(count_totalretweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', user_location='England', sentiment='positive')

        # test first project with None field
        pr = ProjectSocialFactory()
        widget_pk = pr.social_widgets_list.summary_id
        url = reverse('project_social:social_summary_widget', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'authors': 2,
               'countries': 2,
               'languages': 2,
               'likes': 3,
               'negative': 0,
               'neutral': 1,
               'positive': 1,
               'posts': 2,
               'replies': 3,
               'retweets': 3,
               'sources': 1}

        self.assertEqual(json.loads(response.content), res)

        # test second project with filters
        pr = ProjectSocialFactory(country_filter=['USA'], author_filter=['First_name'])
        widget_pk = pr.social_widgets_list.summary_id
        url = reverse('project_social:social_summary_widget', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'authors': 1,
            'countries': 1,
            'languages': 1,
            'likes': 1,
            'negative': 0,
            'neutral': 1,
            'positive': 0,
            'posts': 1,
            'replies': 1,
            'retweets': 1,
            'sources': 1
        }
        self.assertEqual(json.loads(response.content), res)
