from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
import json


class DeletePostTests(APITestCase):
    def test_delete_post(self):
        user = User.objects.create(username='Admin')
        self.client.force_login(user)
        
        post1 = PostFactory()
        post2 = PostFactory()
        project = ProjectFactory()
        project.posts.set([post1, post2])

        data = {'project_pk': project.id}

        self.assertEqual(project.posts.all().count(), 2)

        response = self.client.post(f'/api/search', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['posts']), 2)

        response = self.client.get(f'/api/project/{project.id}/{post1.id}/delete', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(project.posts.all().count(), 2)

        response = self.client.post(f'/api/search', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)['posts']), 1)
