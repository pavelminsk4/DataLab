from common.factories.project_social import ProjectSocialFactory
from common.factories.tweet_binder_post import TweetBinderPostFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class AuthorsByGenderests(APITestCase):
  def test_response_list(self):
    TweetBinderPostFactory(user_alias='@user1', user_gender='female')
    TweetBinderPostFactory(user_alias='@user2', user_gender='male')
    TweetBinderPostFactory(user_alias='@user3', user_gender='undefinded')
    TweetBinderPostFactory(user_alias='@user4', user_gender='male')

    pr = ProjectSocialFactory()
    widget_pk = pr.social_widgets_list.authors_by_gender_id
    url = reverse('project_social:social_authors_by_gender', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'male': 2, 'female': 1, 'undefinded': 1}
    self.assertEqual(json.loads(response.content), res)
