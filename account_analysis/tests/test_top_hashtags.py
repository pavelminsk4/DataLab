from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopHashtagsWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(count_hashtags=2, hashtags=['test', 'post'], count_favorites='5')
        TweetBinderPostFactory()
        TweetBinderPostFactory()
        TweetBinderPostFactory(count_favorites='4')
        TweetBinderPostFactory()
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.top_hashtags_id
        url = reverse('account_analysis:top_hashtags', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [['test', 17], ['post', 6]]
        self.assertEqual(json.loads(response.content), res)
