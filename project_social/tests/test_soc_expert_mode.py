from common.factories.project_social import ProjectSocialFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from project_social.social_parser import SocialParser
from common.factories.tweet_binder_post import TweetBinderPostFactory
from tweet_binder.models import TweetBinderPost
from rest_framework import status
from django.urls import reverse
import json


class TestSocialParser(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(text='bird', sentiment='positive')
        TweetBinderPostFactory(text='bird dog', sentiment='negative')
        TweetBinderPostFactory(text='dog cat', sentiment='positive')
        TweetBinderPostFactory(text='bird', locationString='Scotland')
        TweetBinderPostFactory(text='wolf cat bear', locationString='Scotland')
        TweetBinderPostFactory(text='cat fish', sentiment='positive')
        TweetBinderPostFactory(text='wolf', sentiment='positive')
        TweetBinderPostFactory(text='cat bear cow', user_followers=100)
        TweetBinderPostFactory(text='bear bird wolf cat', user_followers=200)
        TweetBinderPostFactory(text='dog bird wolf', user_followers=200)

    def test_simple_parse(self):
        posts = TweetBinderPost.objects.filter(SocialParser('bird').get_filter_query())
        self.assertEqual(posts.count(), 5)
        posts = TweetBinderPost.objects.filter(SocialParser('bird or dog').get_filter_query())
        self.assertEqual(posts.count(), 6)
        posts = TweetBinderPost.objects.filter(SocialParser('bird and not location:Scotland').get_filter_query())
        self.assertEqual(posts.count(), 4)
        posts = TweetBinderPost.objects.filter(SocialParser('(bird or wolf) and sentiment:positive').get_filter_query())
        self.assertEqual(posts.count(), 2)
        posts = TweetBinderPost.objects.filter(SocialParser('(cow or wolf) and followers: >150').get_filter_query())
        self.assertEqual(posts.count(), 2)
        posts = TweetBinderPost.objects.filter(SocialParser('(cow or wolf) and followers: =100').get_filter_query())
        self.assertEqual(posts.count(), 3)

    def test_search_with_expert_filter(self):
        self.client.force_login(UserFactory())
        data = {
            'keywords': ['cat'],
            'exceptions': [],
            'additions': [],
            'country': [],
            'language': [],
            'sentiment': [],
            'date_range': ['2018-09-02T06:44:00Z', '2024-09-30T06:44:00Z'],
            'source': [],
            'author': [],
            'posts_per_page': 20,
            'page_number': 1,
            'author_dimensions': [],
            'language_dimensions': [],
            'country_dimensions': [],
            'source_dimensions': [],
            'sentiment_dimensions': [],
            'query_filter': '(cow or wolf) and followers:>150',
            'expert_mode': True,
        }
        url = reverse('project_social:twitter_posts_search')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['num_posts'], 2)

    def test_widget_posts_with_expert_filter(self):
        pr = ProjectSocialFactory(query_filter='wolf and not (bird or cat)', expert_mode=True)
        widget_pk = pr.social_widgets_list.top_keywords_id
        url = reverse('project_social:social_top_keywords', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {'key': 'wolf', 'value': 1.0},
        ]
        self.assertEqual(json.loads(response.content), res)
