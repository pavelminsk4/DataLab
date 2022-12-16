from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class SentimentForPeriodWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink1 = Feedlinks.objects.create(country = 'England')
    flink2 = Feedlinks.objects.create(country = 'USA')
    flink3 = Feedlinks.objects.create(country = 'USA', source1='Time')
    flink4 = Feedlinks.objects.create(country = 'Canada', source1='BBC')
    sp1 = Speech.objects.create(language='English (United States)')
    sp2 = Speech.objects.create(language='Spain')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    post3 = Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp1, entry_published=datetime(2021, 10, 3, 6, 37), entry_author='AFP', sentiment='negative')
    post4 = Post.objects.create(feedlink=flink2, entry_title='4 post title', feed_language=sp2, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='negative')
    post5 = Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='positive')
    post6 = Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2022, 10, 3, 6, 37), entry_author='EFE', sentiment='neutral')
    post7 = Post.objects.create(feedlink=flink4, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral')
    post8 = Post.objects.create(feedlink=flink4, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='', sentiment='neutral')
    # test first project with None field
    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), source_filter='', author_filter='', language_filter='', creator=user)
    url = reverse('widgets:sentiment_for_period_widget', kwargs={'pk':pr.pk})
    data = {
            'smpl_freq': "day"
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'2021-09-03 00:00:00+00:00': {'negative': 1, 'neutral': 1, 'positive': 0}},
            {'2021-10-03 00:00:00+00:00': {'negative': 1, 'neutral': 0, 'positive': 0}},
            {'2022-09-03 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 1}},
            {'2022-10-03 00:00:00+00:00': {'negative': 0, 'neutral': 1, 'positive': 0}},
            {'2023-09-03 00:00:00+00:00': {'negative': 0, 'neutral': 2, 'positive': 0}}
          ]
    self.assertEqual(json.loads(response.content), res)
