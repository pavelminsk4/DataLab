from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.feedlink import FeedlinkFactory
from common.factories.project import ProjectFactory
from comparison.models import ProjectComparison
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.urls import reverse
import json


class ComparisonOnlineSummaryTests(APITestCase):
    def setUp(self):
        pr = ProjectFactory(title='Girlfriend')
        prcmpr = ProjectComparisonFactory()
        ComparisonItemFactory(module_project_id=pr.id, project=prcmpr)

    def test_summary_feature_online(self):
        PostFactory(feedlink=FeedlinkFactory(source1='Prospero', country='Space'), entry_summary='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:summary', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)), 8)
        self.assertEqual(json.loads(response.content)[0]['widget_name'], 'summary')
        self.assertEqual(json.loads(response.content)[1]['widget_name'], 'content_volume')
        self.assertEqual(json.loads(response.content)[2]['widget_name'], 'top_authors')
        self.assertEqual(json.loads(response.content)[3]['widget_name'], 'sentiment')
        self.assertEqual(json.loads(response.content)[4]['widget_name'], 'top_sources')
        self.assertEqual(json.loads(response.content)[5]['widget_name'], 'top_keywords')
        self.assertEqual(json.loads(response.content)[6]['widget_name'], 'top_languages')
        self.assertEqual(json.loads(response.content)[7]['widget_name'], 'top_countries')
