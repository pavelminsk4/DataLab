from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class SentimentTop10CountriesWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink1 = Feedlinks.objects.create(country = 'England')
    flink2 = Feedlinks.objects.create(country = 'USA')
    flink3 = Feedlinks.objects.create(country = 'USA', source1='Time')
    flink4 = Feedlinks.objects.create(country = 'Canada', source1='BBC')
    sp1 = Speech.objects.create(language='English (United States)')
    sp2 = Speech.objects.create(language='Spain')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    post3 = Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp1, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='negative', summary_vector=[])
    post4 = Post.objects.create(feedlink=flink2, entry_title='4 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='negative', summary_vector=[])
    post5 = Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='positive', summary_vector=[])
    post6 = Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', sentiment='neutral', summary_vector=[])
    post7 = Post.objects.create(feedlink=flink4, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    post8 = Post.objects.create(feedlink=flink4, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='', sentiment='neutral', summary_vector=[])
    # test first project with None field
    pr1 = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), source_filter='', author_filter='', language_filter='', creator=user)
    widget_pk = pr1.widgets_list_2.sentiment_top_10_countries_widget_id
    url = reverse('widgets:sentiment_top_10_countries_widget', kwargs={'pk':pr1.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'USA': [
                    {'sentiment': 'negative', 'sentiment_count': 2},
                    {'sentiment': 'neutral', 'sentiment_count': 1},
                    {'sentiment': 'positive', 'sentiment_count': 1}
                  ],
           'Canada': [
                      {'sentiment': 'neutral', 'sentiment_count': 2},
                      {'sentiment': 'negative', 'sentiment_count': 0},
                      {'sentiment': 'positive', 'sentiment_count': 0}
                     ],
           'England': [
                        {'sentiment': 'neutral', 'sentiment_count': 2},
                        {'sentiment': 'negative', 'sentiment_count': 0},
                        {'sentiment': 'positive', 'sentiment_count': 0}
                      ]
          }
    self.assertEqual(json.loads(response.content), res)
