from project.models import Project, Post, Feedlinks, Speech
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from accounts.models import Department
from rest_framework import status
from django.urls import reverse
from widgets.models import *


class InstantReportTests(APITestCase):
    def test_instant_reposrts(self):
        user = UserFactory()
        dep = Department.objects.create(departmentname='First Dep')
        user.user_profile.department = dep
        flink = Feedlinks.objects.create(country='England')
        sp = Speech.objects.create(language='English (United States)')

        Post.objects.create(id=1, feedlink=flink, entry_title='First post title Keyword', feed_language=sp, entry_published="2022-10-11T00:00:00Z", summary_vector=[])
        Post.objects.create(id=2, feedlink=flink, entry_title='Second post title Keyword', feed_language=sp, entry_published="2022-10-12T00:00:00Z", summary_vector=[])
        Post.objects.create(id=3, feedlink=flink, entry_title='Third post title Keyword', feed_language=sp, entry_published="2022-10-13T00:00:00Z", summary_vector=[])
        pr = Project.objects.create(
            title='Project1',
            keywords=['Keyword'],
            additional_keywords=[],
            ignore_keywords=[],
            start_search_date="2022-10-10T00:00:00Z",
            end_search_date="2022-10-16T00:00:00Z",
            creator=user,
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

        url = reverse('instantly_report', kwargs={'proj_pk': pr.pk})
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
