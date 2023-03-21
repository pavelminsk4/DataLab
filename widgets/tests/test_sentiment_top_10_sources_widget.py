from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class SentimentTop10SourcesWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink3 = Feedlinks.objects.create(country = 'USA', source1='Time')
    flink4 = Feedlinks.objects.create(country = 'Canada', source1='BBC')
    sp2 = Speech.objects.create(language='Spain')
    Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='positive', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', sentiment='neutral', summary_vector=[])
    Post.objects.create(feedlink=flink4, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', sentiment='neutral', summary_vector=[])
    Post.objects.create(feedlink=flink4, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='', sentiment='neutral', summary_vector=[])
    # test first project with None field
    pr1 = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), country_filter='', author_filter='', language_filter='', creator=user)
    widget_pk = pr1.widgets_list_2.sentiment_top_10_sources_widget_id
    url = reverse('widgets:sentiment_top_10_sources_widget', kwargs={'pk':pr1.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = {'BBC': [
                      {'sentiment': 'neutral', 'sentiment_count': 2},
                      {'sentiment': 'negative', 'sentiment_count': 0},
                      {'sentiment': 'positive', 'sentiment_count': 0}
                    ],
           'Time': [
                      {'sentiment': 'neutral', 'sentiment_count': 1},
                      {'sentiment': 'positive', 'sentiment_count': 1},
                      {'sentiment': 'negative', 'sentiment_count': 0}
                    ],
            }
    self.assertEqual(json.loads(response.content), res)
