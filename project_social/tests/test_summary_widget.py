from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class SummaryWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', sentiment_vote='neutral', text='First twitter post', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', sentiment_vote='positive', text='Second twitter post', creation_date=datetime(2020, 10, 10))
    # test first project with None field
    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)
    widget_pk = pr.social_widgets_list.summary_id
    url = reverse('project_social:social_summary_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'authors': 2,
           'countries': 2,
           'languages': 2,
           'likes': 3,
           'neg': 0,
           'neut': 1,
           'pos': 1,
           'posts': 2,
           'replies': 3,
           'retweets': 3,
           'sources': 1}
    
    self.assertEqual(json.loads(response.content), res)

    # test second project with filters
    pr = ProjectSocial.objects.create(title='Second Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), country_filter=['USA'], author_filter=['First_name'], source_filter=[], creator=user)
    widget_pk = pr.social_widgets_list.summary_id
    url = reverse('project_social:social_summary_widget', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'authors': 1,
           'countries': 1,
           'languages': 1,
           'likes': 1,
           'neg': 0,
           'neut': 1,
           'pos': 0,
           'posts': 1,
           'replies': 1,
           'retweets': 1,
           'sources': 1}
    
    self.assertEqual(json.loads(response.content), res)
