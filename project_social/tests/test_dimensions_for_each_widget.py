from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class DimensionsForEachWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', 
                                   sentiment='neutral', text='First twitter post', date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', 
                                   sentiment='positive', text='Second twitter post', date=datetime(2020, 10, 10), creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='3_name', locationString='USA', 
                                   sentiment='neutral', text='3 twitter post', date=datetime(2021, 10, 10), creation_date=datetime(2020, 10, 10))
    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_dimensions=[], language_dimensions=[], creator=user)
    widget_pk = pr.social_widgets_list.content_volume_by_top_authors_id
    url = reverse('project_social:dimensions_for_each_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    data = {
            'author_dim_pivot': [],
            'country_dim_pivot': [],
            'source_dim_pivot': [],
            'language_dim_pivot': ["En"], 
            'sentiment_dim_pivot': []
            }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content), {})
    url = reverse('project_social:social_content_volume_by_top_languages', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'En': [
                    {'date': '2020-10-10 00:00:00+00:00', 'post_count': 1},
                    {'date': '2021-10-10 00:00:00+00:00', 'post_count': 1}
                   ]
            }
          ]
    self.assertEqual(json.loads(response.content), res)
