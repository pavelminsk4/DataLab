from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.project_social import ProjectSocialFactory
from comparison.models import ProjectComparison
from rest_framework.test import APITestCase
from django.urls import reverse
import json


class ComparisonSocialInfluencersTests(APITestCase):
    def setUp(self):
        pr = ProjectSocialFactory(title='Girlfriend')
        prcmpr = ProjectComparisonFactory()
        ComparisonItemFactory(module_project_id=pr.id, module_type='ProjectSocial', project=prcmpr)

    def test_influencers_feature_social(self):
        TweetBinderPostFactory(text='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:influencers', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)), 7)
        self.assertEqual(json.loads(response.content)[0]['widget_name'], 'top_sharing_sources')
        self.assertEqual(json.loads(response.content)[1]['widget_name'], 'authors_by_sentiment')
        self.assertEqual(json.loads(response.content)[2]['widget_name'], 'overall_top_authors')
        self.assertEqual(json.loads(response.content)[3]['widget_name'], 'top_authors_by_gender')
        self.assertEqual(json.loads(response.content)[4]['widget_name'], 'authors_by_location')
        self.assertEqual(json.loads(response.content)[5]['widget_name'], 'authors_by_gender')
        self.assertEqual(json.loads(response.content)[6]['widget_name'], 'authors_by_language')