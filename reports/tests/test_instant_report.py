from project.models import Project, Post, Feedlinks, Speech
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from accounts.models import department
from reports.models import Templates
from rest_framework import status
from django.urls import reverse
from widgets.models import *
from unittest import skip

class InstantReportTests(APITestCase):
  def test_instant_reposrts(self):
    user = User.objects.create(username='Fox')
    dep = department.objects.create(
      departmentname = 'First Dep',
    )
    user.user_profile.department = dep
    flink = Feedlinks.objects.create(country='England')
    sp = Speech.objects.create(language='English (United States)')
    post1 = Post.objects.create(id=1, feedlink=flink, entry_title='First post title Keyword', feed_language=sp, entry_published="2022-10-11T00:00:00Z", summary_vector=[])
    post2 = Post.objects.create(id=2, feedlink=flink, entry_title='Second post title Keyword', feed_language=sp, entry_published="2022-10-12T00:00:00Z", summary_vector=[])
    post3 = Post.objects.create(id=3, feedlink=flink, entry_title='Third post title Keyword', feed_language=sp, entry_published="2022-10-13T00:00:00Z", summary_vector=[])
    template = Templates.objects.create(title='Temp', layout_file='static/report_templates/RSDC_Export_Template_AR.docx')
    pr = Project.objects.create(
        title='Project1',
        keywords=['Keyword'],
        additional_keywords=[], 
        ignore_keywords=[],
        start_search_date="2022-10-10T00:00:00Z",
        end_search_date="2022-10-16T00:00:00Z",
        creator=user,
        report_template=template,
        )
    pr.widgets_list_2.summary.is_active = True
    pr.widgets_list_2.volume.is_active = True
    pr.widgets_list_2.top_authors.is_active = True
    pr.widgets_list_2.top_sources.is_active = True
    pr.widgets_list_2.top_countries.is_active = True
    pr.widgets_list_2.top_languages.is_active = True
    pr.widgets_list_2.content_volume_top_authors.is_active = True
    pr.widgets_list_2.content_volume_top_countries.is_active = True
    pr.widgets_list_2.content_volume_top_sources.is_active = True
    pr.widgets_list_2.sentiment_for_period.is_active = True
    pr.widgets_list_2.sentiment_top_authors.is_active = True
    pr.widgets_list_2.sentiment_top_countries.is_active = True
    pr.widgets_list_2.sentiment_top_languages.is_active = True
    pr.widgets_list_2.sentiment_top_sources.is_active = True
    pr.widgets_list_2.clipping_feed_content.is_active = True
    url = reverse('instantly_report', kwargs={'proj_pk':pr.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
