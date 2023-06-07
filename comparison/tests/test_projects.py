from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from project.models import Project
from django.urls import reverse
import json


class ComparisonProjectsTests(APITestCase):
    def setUp(self):
        UserFactory(username='user', password='user')
        profile = Profile.objects.first()
        dep = DepartmentFactory()
        profile.department = dep
        profile.save()
        ws = WorkspaceFactory(department=dep, title='Avril Lavigne')
        ProjectFactory(workspace=ws, title='Girlfriend')

    def test_get_project_list(self):
        self.client.force_login(User.objects.first())
        url = reverse('comparison:projects_list')
        response = self.client.post(url, format='json')
        res = {
            'Online': [{'Avril Lavigne': [{'id': Project.objects.first().id, 'title': 'Girlfriend'}]}],
            'Social': []
        }
        self.assertEqual(json.loads(response.content), res)
