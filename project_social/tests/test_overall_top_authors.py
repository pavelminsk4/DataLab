from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class OverallTopAuthorsTest(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(count_retweets='1', user_gender='male', count_favorites='1', count_replies='1', user_name='First_name', user_alias='@first', sentiment='neutral')
        TweetBinderPostFactory(count_retweets='2', user_gender='male', count_favorites='2', count_replies='2', user_name='First_name', user_alias='@first', sentiment='positive')
        TweetBinderPostFactory(count_retweets='3', user_gender='female', count_favorites='9', count_replies='2', user_name='Second_name', user_alias='@second', sentiment='positive')
        ProjectSocialFactory()

    def test_top_overall_authors(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.overall_top_authors_id
        url = reverse('project_social:social_overall_top_authors', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            {
                'name': 'First_name',
                'alias': '@first',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  1,
                },
                'gender': 'male',
                'posts': 2,
                'media_type': 'Twitter',
                'reach': 100,
                'engagements': 6,
            },
            {
                'name': 'Second_name',
                'alias': '@second',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  0,
                },
                'gender': 'female',
                'posts': 1,
                'media_type': 'Twitter',
                'reach': 100,
                'engagements': 12,
            },
        ]
        self.assertEqual(json.loads(response.content), res)

    def test_top_authors_by_gender(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_authors_by_gender_id
        url = reverse('project_social:social_top_authors_by_gender', kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [
            [{
                'name': 'First_name',
                'alias': '@first',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  1,
                },
                'gender': 'male',
                'posts': 2,
                'media_type': 'Twitter',
                'reach': 100,
                'engagements': 6,
            }],
            [{
                'name': 'Second_name',
                'alias': '@second',
                'picture': None,
                'sentiments': {
                    'positive': 1,
                    'negative': 0,
                    'neutral':  0,
                },
                'gender': 'female',
                'posts': 1,
                'media_type': 'Twitter',
                'reach': 100,
                'engagements': 12,
            }]
        ]
        self.assertEqual(json.loads(response.content), res)
