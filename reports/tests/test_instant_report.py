from rest_framework.test import APITestCase
from django.db import models
from rest_framework import status
from project.models import Project, Post, Feedlinks, Speech
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
import time
from widgets.models import *
from reports.models import Templates

class InstantReportTests(APITestCase):
  def test_instant_reposrts(self):
    user = User.objects.create(username='Fox')
    flink = Feedlinks.objects.create(country='England')
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(id=1, feedlink=flink, entry_title='First post title Keyword', feed_language=sp, entry_published=datetime(2022, 10, 11, 6, 37))
    post2 = Post.objects.create(id=2, feedlink=flink, entry_title='Second post title Keyword', feed_language=sp, entry_published=datetime(2022, 10, 12, 6, 37))
    post3 = Post.objects.create(id=3, feedlink=flink, entry_title='Third post title Keyword', feed_language=sp, entry_published=datetime(2023, 10, 13, 6, 37))    
    template = Templates.objects.create(title='Temp', layout_file='static/report_templates/RSDC_Export_Template_AR.docx')
    pr = Project.objects.create(
        title='Project1',
        keywords=['Keyword'],
        additional_keywords=[], 
        ignore_keywords=[],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user,
        report_template=template,
        )
    pr.widgets_list_2.summary_widget.is_active = True
    pr.widgets_list_2.volume_widget.is_active = True
    pr.widgets_list_2.top_10_authors_by_volume_widget.is_active = True
    pr.widgets_list_2.top_10_brands_widget.is_active = True
    pr.widgets_list_2.top_10_countries_widget.is_active = True
    pr.widgets_list_2.top_10_languages_widget.is_active = True
    pr.widgets_list_2.content_volume_top_10_authors_widget.is_active = True
    pr.widgets_list_2.content_volume_top_10_countries_widget.is_active = True
    pr.widgets_list_2.content_volume_top_10_source_widget.is_active = True
    pr.widgets_list_2.sentiment_for_period_widget.is_active = True
    pr.widgets_list_2.sentiment_top_10_authors_widget.is_active = True
    pr.widgets_list_2.sentiment_top_10_countries_widget.is_active = True
    pr.widgets_list_2.sentiment_top_10_languages_widget.is_active = True
    pr.widgets_list_2.sentiment_top_10_sources_widget.is_active = True
    pr.widgets_list_2.clipping_feed_content_widget.is_active = True
    url = reverse('instantly_report', kwargs={'proj_pk':pr.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
