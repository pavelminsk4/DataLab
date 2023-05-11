from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
import json
from project.models import Post, Project, Speech, Feedlinks
from django.contrib.auth.models import User

class Top10CountriesWidgetTests(APITestCase):
  def test_response_list(self):
    user = User.objects.create(username='Pablo')
    flink1 = Feedlinks.objects.create(country = 'England')
    flink2 = Feedlinks.objects.create(country = 'USA')
    flink3 = Feedlinks.objects.create(country = 'USA', source1='Time')
    flink4 = Feedlinks.objects.create(country = 'Canada')
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(feedlink=flink1, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post2 = Post.objects.create(feedlink=flink1, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post3 = Post.objects.create(feedlink=flink2, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post4 = Post.objects.create(feedlink=flink2, entry_title='4 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post5 = Post.objects.create(feedlink=flink3, entry_title='5 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post6 = Post.objects.create(feedlink=flink3, entry_title='6 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='EFE', summary_vector=[])
    post7 = Post.objects.create(feedlink=flink4, entry_title='5 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='AFP', summary_vector=[])
    post8 = Post.objects.create(feedlink=flink4, entry_title='6 post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37), entry_author='', summary_vector=[])
    # test first project with None field
    pr1 = Project.objects.create(title='Project1', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), language_filter=sp, author_filter='', source_filter='', creator=user)
    widget_pk = pr1.widgets_list_2.top_countries_id
    url = reverse('widgets:onl_top_countries', kwargs={'pk':pr1.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {'feedlink__country': 'USA', 'country_count': 4},
      {'feedlink__country': 'Canada', 'country_count': 2},
      {'feedlink__country': 'England', 'country_count': 2},
    ]
    self.assertEqual(json.loads(response.content), res)
    # test second project with author, source filters
    pr2 = Project.objects.create(title='Project2', keywords=['post'], additional_keywords=[], ignore_keywords=[], start_search_date=datetime(2020, 10, 10), 
                                end_search_date=datetime(2023, 10, 16), language_filter=sp, author_filter='AFP', source_filter='Time', creator=user)
    widget_pk = pr2.widgets_list_2.top_countries_id
    url = reverse('widgets:onl_top_countries', kwargs={'pk':pr2.pk, 'widget_pk':widget_pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res2 = [
      {'feedlink__country': 'USA', 'country_count': 1},
    ]
    self.assertEqual(json.loads(response.content), res2)
