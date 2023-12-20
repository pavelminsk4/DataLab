from common.factories.project_social import ProjectSocialFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class AuthorsByGenderTests(APITestCase):
    maxDiff = None

    def test_response_list(self):
        TweetBinderPostFactory(user_gender='female')
        TweetBinderPostFactory(user_name='user_2', user_gender='male')
        TweetBinderPostFactory(user_name='user_3', user_gender='undefinded')
        TweetBinderPostFactory(user_name='user_4', user_gender='male')

        pr = ProjectSocialFactory()
        widget_pk = pr.social_widgets_list.authors_by_gender_id
        url = reverse('project_social:social_authors_by_gender', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
                'female': [['First_name', 1]],
                'male': [['user_2', 1], ['user_4', 1]],
              }
        self.assertEqual(json.loads(response.content), res)
