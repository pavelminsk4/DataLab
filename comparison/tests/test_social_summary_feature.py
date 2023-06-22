from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.project_social import ProjectSocialFactory
from comparison.models import ProjectComparison
from rest_framework.test import APITestCase
from django.urls import reverse
import json


class ComparisonSocialSummaryTests(APITestCase):
    def setUp(self):
        pr = ProjectSocialFactory(title='Girlfriend')
        prcmpr = ProjectComparisonFactory()
        ComparisonItemFactory(module_project_id=pr.id, module_type='ProjectSocial', project=prcmpr)

    def test_summary_feature_social(self):
        TweetBinderPostFactory(text='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:summary', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        res = [{
            'Girlfriend':{
                    'Summary': {
                        'posts': 1,
                        'sources': 1,
                        'authors': 1,
                        'countries': 1,
                        'languages': 1,
                        'pos': 0,
                        'neg': 0,
                        'neut': 1,
                        'likes': 1,
                        'replies': 1,
                        'retweets': 1
                    },
                    'Content volume': [{'date': '2020-10-10 00:00:00+00:00', 'created_count': 1}],
                    'Top authors': [{'user_name': 'First_name', 'user_count': 1}],
                    'Sentiment': {'positive': 0, 'negative': 0, 'neutral': 0},
                    'Top keywords': [{'key': 'post', 'value': 1.0}],
                    'Top languages': [{'language': 'En', 'language_count': 1}],
                    'Top locations': [{'locationString': 'Nostramo', 'locations_count': 1}]
            }
        }]
        self.assertEqual(json.loads(response.content), res)
