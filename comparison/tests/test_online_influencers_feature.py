from common.factories.talkwalker_feedlink import TalkwalkerFeedlinksFactory
from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.talkwalker_post import TalkwalkerPostFactory
from common.factories.feedlinks import FeedlinksFactory
from common.factories.project import ProjectFactory
from comparison.models import ProjectComparison
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.urls import reverse
import json, os


class ComparisonOnlineInfluencersTests(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'rss'
        pr = ProjectFactory(title='Girlfriend')
        prcmpr = ProjectComparisonFactory()
        ComparisonItemFactory(module_project_id=pr.id, project=prcmpr)

    def test_influencers_feature_online(self):
        PostFactory(feedlink=FeedlinksFactory(source1='Prospero', country='Space'), entry_summary='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:influencers', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)), 7)
        self.assertEqual(json.loads(response.content)[0]['widget_name'], 'top_sharing_sources')
        self.assertEqual(json.loads(response.content)[1]['widget_name'], 'authors_by_language')
        self.assertEqual(json.loads(response.content)[2]['widget_name'], 'overall_top_sources')
        self.assertEqual(json.loads(response.content)[3]['widget_name'], 'overall_top_authors')
        self.assertEqual(json.loads(response.content)[4]['widget_name'], 'authors_by_location')
        self.assertEqual(json.loads(response.content)[5]['widget_name'], 'authors_by_sentiment')
        self.assertEqual(json.loads(response.content)[6]['widget_name'], 'sources_by_language')


class ComparisonOnlineInfluencersTestsTWL(APITestCase):
    def setUp(self):
        os.environ['POST_LOCATOR'] = 'talkwalker'
        pr = ProjectFactory(title='Girlfriend')
        prcmpr = ProjectComparisonFactory()
        ComparisonItemFactory(module_project_id=pr.id, project=prcmpr)

    def test_influencers_feature_online_tlw(self):
        TalkwalkerPostFactory(feedlink=TalkwalkerFeedlinksFactory(source1='Prospero', country='Space'), entry_summary='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:influencers', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)), 7)
        self.assertEqual(json.loads(response.content)[0]['widget_name'], 'top_sharing_sources')
        self.assertEqual(json.loads(response.content)[1]['widget_name'], 'authors_by_language')
        self.assertEqual(json.loads(response.content)[2]['widget_name'], 'overall_top_sources')
        self.assertEqual(json.loads(response.content)[3]['widget_name'], 'overall_top_authors')
        self.assertEqual(json.loads(response.content)[4]['widget_name'], 'authors_by_location')
        self.assertEqual(json.loads(response.content)[5]['widget_name'], 'authors_by_sentiment')
        self.assertEqual(json.loads(response.content)[6]['widget_name'], 'sources_by_language')
