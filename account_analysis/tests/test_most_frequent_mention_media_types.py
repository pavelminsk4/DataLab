from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class MostFrequentMentionMediaTypeslineWidgetTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(count_links=0, count_textlength=0, count_images=0, videos=None, text = 'First twitter post @First_name')
        TweetBinderPostFactory(count_textlength=0, count_images=0, text = 'First twitter post @First_name')
        TweetBinderPostFactory(count_links=0, text = 'First twitter post @First_name')
        TweetBinderPostFactory(count_images=0, text = 'First twitter post @First_name')
        TweetBinderPostFactory(videos=None)
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.most_frequent_mention_media_types_id
        url = reverse('account_analysis:most_frequent_mention_media_types', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'count_combination': 3,
                'count_link': 2,
                'count_photo': 1,
                'count_text': 2,
                'count_video': 3
              }
        self.assertEqual(json.loads(response.content), res)
