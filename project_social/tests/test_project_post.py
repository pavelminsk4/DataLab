from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.department import DepartmentFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import json


class ProjectPostsTests(APITestCase):
    def test_response_list(self):
        TweetBinderPostFactory.create_batch(5)
        dep = DepartmentFactory()
        pr = ProjectSocialFactory()
        url = reverse('project_social:project_posts', kwargs={'pk': pr.id})
        data = {
            'department_id': dep.id,
            'posts_per_page': 5,
            'page_number': 1,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['posts']), 5)
