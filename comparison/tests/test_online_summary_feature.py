from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.feedlinks import FeedlinksFactory
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
        PostFactory(feedlink=FeedlinksFactory(source1='Prospero', country='Space'), entry_summary='post')
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:summary', kwargs={'pk': pr.id})
        response = self.client.get(url, format='json')
        res = [{
            'Girlfriend': {
                'Summary': {
                    'posts': 1,
                    'sources': 1,
                    'authors': 1,
                    'countries': 1,
                    'languages': 1,
                    'pos': 0,
                    'neg': 0,
                    'neut': 1,
                    'reach': 0
                },
                'Content volume': [{'created_count': 1, 'date': '2020-10-10T00:00:00Z'}],
                'Top authors': [{'entry_author': 'Socrat', 'author_posts_count': 1}],
                'Sentiment': {'positive': 0, 'negative': 0, 'neutral': 1},
                'Top sources': [{'feedlink__source1': 'Prospero', 'brand_count': 1}],
                'Top keywords': [{'key': 'post', 'value': 1.0}],
                'Top languages': [{'feed_language__language': 'English', 'language_count': 1}],
                'Top countries': [{'feedlink__country': 'Space', 'country_count': 1}],
            }
        }]
        self.assertEqual(json.loads(response.content), res)
