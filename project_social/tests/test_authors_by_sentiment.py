from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json

class AuthorsBySentimentTests(APITestCase):
  def test_response_list(self):
    TweetBinderPostFactory(sentiment='neutral')
    TweetBinderPostFactory(user_name='Second_name', sentiment='positive')
    TweetBinderPostFactory(user_name='Second_name', sentiment='positive')
    TweetBinderPostFactory(user_name='New_Name', sentiment='positive')

    pr = ProjectSocialFactory()
    widget_pk = pr.social_widgets_list.authors_by_sentiment_id
    url = reverse('project_social:social_authors_by_sentiment', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {
            'negative': [],
            'neutral': [['First_name', 1]],
            'positive': [['Second_name', 2], ['New_Name', 1]]
          }
    self.assertEqual(json.loads(response.content), res)
