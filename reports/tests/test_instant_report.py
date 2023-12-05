from project.models import Project, Post, Feedlinks, Speech
from common.factories.user import UserFactory
from common.factories.department import DepartmentFactory
from rest_framework.test import APITestCase
from accounts.models import Profile
from rest_framework import status


class InstantReportTests(APITestCase):
    def test_instant_top_reports(self):
        user = UserFactory()

        dep = DepartmentFactory()
        user.user_profile.department = dep
        user.user_profile.role = Profile.REGULAR_USER
        user.user_profile.save()

        flink = Feedlinks.objects.create(country='England')
        sp    = Speech.objects.create(language='English (United States)')
        post1 = Post.objects.create(id=1, feedlink=flink, entry_title='First post title Keyword', feed_language=sp, entry_published="2022-10-11T00:00:00Z", summary_vector=[])
        post2 = Post.objects.create(id=2, feedlink=flink, entry_title='Second post title Keyword', feed_language=sp, entry_published="2022-10-12T00:00:00Z", summary_vector=[])
        post3 = Post.objects.create(id=3, feedlink=flink, entry_title='Third post title Keyword', feed_language=sp, entry_published="2022-10-13T00:00:00Z", summary_vector=[])

        project = Project.objects.create(
            title='Project1',
            keywords=['Keyword'],
            additional_keywords=[],
            ignore_keywords=[],
            start_search_date="2022-10-10T00:00:00Z",
            end_search_date="2022-10-16T00:00:00Z",
            creator=user,
        )

        project.posts.set([post1, post2, post3])

        project.widgets_list_2.top_authors.is_active = True
        project.widgets_list_2.top_sources.is_active = True
        project.widgets_list_2.top_countries.is_active = True
        project.widgets_list_2.top_languages.is_active = True
        project.widgets_list_2.save()

        self.client.force_login(user)
        response = self.client.get(f'/instantly_report/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
