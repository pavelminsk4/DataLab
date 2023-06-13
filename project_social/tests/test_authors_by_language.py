from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class AuthorsByGenderTests(APITestCase):
  def test_authors_by_gender(self):
    TweetBinderPostFactory(user_alias='@1', language='English')
    TweetBinderPostFactory(user_alias='@1', language='English')
    TweetBinderPostFactory(user_alias='@1', language='English')
    TweetBinderPostFactory(user_alias='@2', language='English')
    TweetBinderPostFactory(user_alias='@3', language='Spanish')
    TweetBinderPostFactory(user_alias='@4', language='Polish')
    TweetBinderPostFactory(user_alias='@5', language='English')
    TweetBinderPostFactory(user_alias='@5', language='English')

    pr = ProjectSocialFactory()
    widget_pk = pr.social_widgets_list.top_locations_id
    url = reverse('project_social:social_authors_by_language', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'English': [['@1', 3], ['@5', 2], ['@2', 1]]},
            {'Polish': [['@4', 1]]},
            {'Spanish': [['@3', 1]]}
          ]
    self.assertEqual(json.loads(response.content), res)
