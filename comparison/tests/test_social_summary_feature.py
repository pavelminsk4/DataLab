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
        self.assertEqual(len(json.loads(response.content)), 7)
        self.assertEqual(json.loads(response.content)[0]['widget_name'], 'summary')
        self.assertEqual(json.loads(response.content)[1]['widget_name'], 'content_volume')
