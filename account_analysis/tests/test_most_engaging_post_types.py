from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class MostEngagingPostTypeslineWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(type=['original', 'reply', 'retweet'])
        TweetBinderPostFactory(count_favorites='3', type=['original', 'reply'])
        TweetBinderPostFactory(count_favorites='3', )
        TweetBinderPostFactory(count_retweets='2', count_favorites='2', type=[
                               'original', 'reply', 'retweet'])
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.most_engaging_post_types_id
        url = reverse('account_analysis:most_engaging_post_types_widget', kwargs={
                      'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'replies_engagement': 10,
               'retweets_engagement': 6,
               'tweets_engagement': 10}
        self.assertEqual(json.loads(response.content), res)
