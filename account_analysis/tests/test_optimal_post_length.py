from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class OptimalPostLengthWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory()
        TweetBinderPostFactory(count_textlength=45)
        TweetBinderPostFactory(count_textlength=46)
        TweetBinderPostFactory(count_textlength=91)
        TweetBinderPostFactory(count_textlength=145)
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.optimal_post_length_id
        url = reverse('account_analysis:optimal_post_length_widget', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'from 0 to 45': 2.0,
                'from 140': 2.0,
                'from 46 to 90': 2.0,
                'from 91 to 140': 2.0,
              }
        self.assertEqual(json.loads(response.content), res)
