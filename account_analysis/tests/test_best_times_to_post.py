from common.factories.account_analysis_project import AccountAnalysisProjectFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from account_analysis.models import ProjectAccountAnalysis
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class BestTimesToPostTests(APITestCase):
    def setUp(self):
        count_likes = 100
        for day in range(10, 31):
            for hour in range(20, 21):
                TweetBinderPostFactory(
                    date=f'2020-01-{day}T{hour}:00:00+00:00', count_favorites=f'{count_likes}')
                count_likes -= 1
        AccountAnalysisProjectFactory()

    def test_response_list(self):
        pr = ProjectAccountAnalysis.objects.first()
        widget_pk = pr.account_analysis_widgets_list.best_times_to_post_id
        url = reverse('account_analysis:best_times_to_post',
                      kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [{'date': 'Friday',
                'engagements': 94.0,
                'likes': 279,
                'reply': 3,
                'retweets': 3},
               {'date': 'Saturday',
                'engagements': 93.0,
                'likes': 276,
                'reply': 3,
                'retweets': 3},
               {'date': 'Sunday',
                'engagements': 92.0,
                'likes': 273,
                'reply': 3,
                'retweets': 3},
               {'date': 'Monday',
                'engagements': 91.0,
                'likes': 270,
                'reply': 3,
                'retweets': 3},
               {'date': 'Tuesday',
                'engagements': 90.0,
                'likes': 267,
                'reply': 3,
                'retweets': 3}]
        self.assertEqual(json.loads(response.content), res)
