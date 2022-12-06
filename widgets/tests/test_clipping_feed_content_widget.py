from project.models import Project, Post, Feedlinks, Speech
from widgets.models import ClippingFeedContentWidget
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json

class WidgetTests(APITestCase):
  def test_widgett(self):
    user = User.objects.create(username='John')
    flink = Feedlinks.objects.create()
    sp = Speech.objects.create(language='English (United States)')
    pr1 = Project.objects.create(title='Project1', keywords=['Keyword'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    pr2 = Project.objects.create(title='Project2', keywords=['Apple'], start_search_date=datetime(2022, 10, 10), end_search_date=datetime(2022, 10, 16), creator=user)
    post1 = Post.objects.create(id=1, feedlink=flink, entry_title='First post title', feed_language=sp, entry_published=datetime(2021, 9, 3, 6, 37))
    post2 = Post.objects.create(id=2, feedlink=flink, entry_title='Second post title', feed_language=sp, entry_published=datetime(2022, 9, 3, 6, 37))
    post3 = Post.objects.create(id=3, feedlink=flink, entry_title='Third post title', feed_language=sp, entry_published=datetime(2023, 9, 3, 6, 37))
    clipped_post1 = ClippingFeedContentWidget.objects.create(project=pr1, post=post1)
    clipped_post2 = ClippingFeedContentWidget.objects.create(project=pr1, post=post2)
    clipped_post3 = ClippingFeedContentWidget.objects.create(project=pr2, post=post3)
    
    url = reverse('widgets:clipping_feed_content_widget', kwargs={'pk': pr1.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    pst1 = {
        'post__id':2,
        'post__entry_title':'Second post title',
        'post__entry_published':"2022-09-03T06:37:00Z",
        'post__entry_summary':None,
        'post__entry_author':None,
        'post__entry_links_href':None,
        'post__entry_media_thumbnail_url':None,
        'post__entry_media_content_url':None,
        'post__feed_image_href':None,
        'post__feed_image_link':None,
        'post__feed_language__language':'English (United States)',
        'post__feedlink__country':None,
        'post__feedlink__source1':None,
        'post__feedlink__sourceurl':None,
        'post__sentiment':"neutral",
        'post__feedlink__alexaglobalrank':0,
      }
    pst2 = {
        'post__id':1,
        'post__entry_title':'First post title',
        'post__entry_published':"2021-09-03T06:37:00Z",
        'post__entry_summary':None,
        'post__entry_author':None,
        'post__feed_image_href':None,
        'post__entry_media_thumbnail_url':None,
        'post__entry_media_content_url':None,
        'post__entry_links_href':None,
        'post__feed_image_link':None,
        'post__feed_language__language':'English (United States)',
        'post__feedlink__country':None,
        'post__feedlink__source1':None,
        'post__feedlink__sourceurl':None,
        'post__sentiment':"neutral",
        'post__feedlink__alexaglobalrank':0,
      }
    self.assertEqual(json.loads(response.content), [pst2, pst1])
