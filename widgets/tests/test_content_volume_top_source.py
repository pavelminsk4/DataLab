from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class ContentVolumeTop5SourcesWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink1 = Feedlinks.objects.create(country = 'England', source1='BBC')
    flink2 = Feedlinks.objects.create(country = 'USA', source1='Time')
    flink3 = Feedlinks.objects.create(country = 'USA', source1='BBC')
    flink4 = Feedlinks.objects.create(country = 'Canada', source1='BBC')
    sp1 = Speech.objects.create(language='English (United States)')
    sp2 = Speech.objects.create(language='Spain')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp1, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp1, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post3 = Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp1, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post4 = Post.objects.create(feedlink=flink2, entry_title='4 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post5 = Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post6 = Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[])
    post7 = Post.objects.create(feedlink=flink4, entry_title='5 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post8 = Post.objects.create(feedlink=flink4, entry_title='6 post title', feed_language=sp2, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='', summary_vector=[])
    # test first project with None field
    pr1 = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), country_filter='', author_filter='', language_filter='', creator=user)
    widget_pk = pr1.widgets_list_2.content_volume_top_sources_id
    url = reverse('widgets:onl_content_volume_top_sources', kwargs={'pk':pr1.pk, 'widget_pk':widget_pk})
    data = {
            'aggregation_period': 'day'
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res1 = [
            {'BBC': [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 1},
                      {'date': '2022-09-03 00:00:00+00:00', 'post_count': 1},
                      {'date': '2023-09-03 00:00:00+00:00', 'post_count': 4}
                      ]},
            {'Time': [{'date': '2021-09-03 00:00:00+00:00', 'post_count': 0},
                      {'date': '2022-09-03 00:00:00+00:00', 'post_count': 0},
                      {'date': '2023-09-03 00:00:00+00:00', 'post_count': 2}
                      ]},
            ]
    self.assertEqual(json.loads(response.content), res1)
