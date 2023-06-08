from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class TopKeywordsTests(APITestCase):
    def setUp(self):
        TweetBinderPostFactory(text='First twitter', sentiment='positive')
        TweetBinderPostFactory(text='Second twitter post', sentiment='positive')
        ProjectSocialFactory(keywords=['twitter'])

    def test_top_keywords_api(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.top_keywords_id
        url = reverse('project_social:social_top_keywords',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = [{'key': 'twitter', 'value': 1.0}, {'key': 'post', 'value': 0.5}]
        self.assertEqual(json.loads(response.content), res)

    def test_sentiment_top_keywords_api(self):
        pr = ProjectSocial.objects.first()
        widget_pk = pr.social_widgets_list.sentiment_top_keywords_id
        url = reverse('project_social:social_sentiment_top_keywords',kwargs={'pk': pr.pk, 'widget_pk': widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {'negative': [],
               'neutral': [],
               'positive': [{'key': 'twitter', 'value': 1.0}, {'key': 'post', 'value': 0.5}]}
        self.assertEqual(json.loads(response.content), res)
