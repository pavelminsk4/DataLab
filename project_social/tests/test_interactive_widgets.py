from tweet_binder.models import TweetBinderPost
from project_social.models import ProjectSocial
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class InteractiveWidgetsTests(APITestCase):
  def setUp(self):
    user = User.objects.create(username='Pablo')
    TweetBinderPost.objects.create(post_id='1', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='First_name', locationString='USA', 
                                   sentiment='neutral', text='First twitter post', date=datetime(2020, 10, 10), user_gender='male', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='2', count_retweets='2', count_favorites='2', count_replies='2', language='Sp', user_name='Second_name', locationString='England', 
                                   sentiment='positive', text='Second twitter post', date=datetime(2020, 10, 10), user_gender='female', creation_date=datetime(2020, 10, 10))
    TweetBinderPost.objects.create(post_id='3', count_retweets='1', count_favorites='1', count_replies='1', language='En', user_name='3_name', locationString='USA', 
                                   sentiment='neutral', text='3 twitter post', date=datetime(2021, 10, 10), user_gender='undefined', creation_date=datetime(2021, 10, 10))
    pr = ProjectSocial.objects.create(title='Project', keywords=['twitter'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                      end_search_date=datetime(2023, 10, 16), country_filter=[], author_filter=[], source_filter=[], creator=user)

  def test_top_languages(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.top_languages_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(text='Second twitter post').pk
    data = {
      'first_value': ['Sp'],
      'second_value': [''],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_top_locations(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.top_locations_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(text='Second twitter post').pk
    data = {
      'first_value': ['England'],
      'second_value': [''],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_top_authors(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.top_authors_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['First_name'],
      'second_value': [''],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)      

  def test_sentiment_authors(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.sentiment_authors_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['neutral'],
      'second_value': ['First_name'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_sentiment_locations(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.sentiment_locations_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['neutral'],
      'second_value': ['USA'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)                    

  def test_sentiment_languages(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.sentiment_languages_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['neutral'],
      'second_value': ['En'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_content_volume_by_top_authors(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.content_volume_by_top_authors_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['First_name'],
      'second_value': [''],
      'dates': [datetime(2020, 10, 10), datetime(2022, 10, 10)],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_sentiment_by_gender(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.sentiment_by_gender_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['neutral'],
      'second_value': ['male'],
      'dates': [],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)                        
  
  def test_content_volume(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.content_volume_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': [''],
      'second_value': [''],
      'dates': [datetime(2020, 10, 10), datetime(2020, 10, 10)],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)

  def test_sentiment(self):
    pr = ProjectSocial.objects.first()
    widget_pk = pr.social_widgets_list.sentiment_id
    url = reverse('project_social:social_interactive_widgets', kwargs={'project_pk':pr.pk, 'widget_pk':widget_pk})
    post_id = TweetBinderPost.objects.all().get(user_name='First_name').pk
    data = {
      'first_value': ['neutral'],
      'second_value': [''],
      'dates':[datetime(2020, 10, 10), datetime(2020, 10, 10)],
      'posts_per_page': 10,
      'page_number': 1,
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.loads(response.content)['posts'][0]['id'], post_id)
