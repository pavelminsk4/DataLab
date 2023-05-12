from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class OptimalNumberOfHashtagsWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(count_hashtags=2, hashtags=['test', 'post'], count_favorites='5')
        TweetBinderPostFactory(count_hashtags=0, hashtags=[])
        TweetBinderPostFactory()
        TweetBinderPostFactory(count_favorites='4')
        TweetBinderPostFactory(count_hashtags=4, hashtags=['test', 'goodbyeamerica', 'catdogandmanymanymanymanymanymanywords', 'like'], count_favorites='5')
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.optimal_number_of_hashtags_id
        url = reverse('account_analysis:optimal_number_of_hashtags', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = { 
                'count_from_1_to_2': 3,
                'count_from_3_to_4': 1,
                'count_from_5': 0,
                'count_zero': 1,
                'engagement_from_1_to_2': 13,
                'engagement_from_3_to_4': 6,
                'engagement_from_5': 0,
                'engagement_zero': 2
              }
        self.assertEqual(json.loads(response.content), res)
