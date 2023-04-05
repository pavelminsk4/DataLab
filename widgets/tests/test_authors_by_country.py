from project.models import Project, Post, Feedlinks, Speech
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json


class AuthorsByCountryTests(APITestCase):
  def test_authors_by_country(self):
    user = User.objects.create(username='Vikernes')

    flink1 = Feedlinks.objects.create(source1='one_source', country = 'England')
    flink2 = Feedlinks.objects.create(source1='two_source', country = 'USA')
    flink3 = Feedlinks.objects.create(source1='third_source', country = 'Greece')
    sp = Speech.objects.create(language='English (United States)')
    Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='4 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[])

    pr = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10),
                                end_search_date=datetime(2023, 10, 16), language_filter=sp, author_filter='', source_filter='', creator=user)
    widget_pk = pr.widgets_list_2.authors_by_country_id
    url = reverse('widgets:authors_by_country', kwargs={'pk':pr.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
            {'feedlink__country': 'Greece', 'author_count': 2},
            {'feedlink__country': 'England', 'author_count': 1},
            {'feedlink__country': 'USA', 'author_count': 1},
          ]
    self.assertEqual(json.loads(response.content), res)
