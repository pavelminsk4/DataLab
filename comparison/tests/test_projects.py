from common.factories.comparison_item import ComparisonItemFactory
from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.workspace_comparison import WorkspaceComparisonFactory
from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from common.factories.user import UserFactory
from comparison.models import ProjectComparison, WorkspaceComparison
from rest_framework.test import APITestCase
from accounts.models import Profile, department
from project.models import Project
from django.urls import reverse
import json


class ComparisonProjectsTests(APITestCase):
    def setUp(self):
        user = UserFactory()
        profile = Profile.objects.first()
        dep = DepartmentFactory()
        profile.department = dep
        profile.save()
        ws = WorkspaceFactory(department=dep, title='Avril Lavigne')
        pr = ProjectFactory(workspace=ws, title='Girlfriend')
        wscmpr = WorkspaceComparisonFactory(department=dep)
        prcmpr = ProjectComparisonFactory(workspace=wscmpr)
        ComparisonItemFactory(module_project_id=pr.id, project=prcmpr)
        self.client.force_login(user)

    def test_get_project_list(self):
        url = reverse('comparison:projects_list')
        response = self.client.post(url, format='json')
        res = {
            'Online': [{'Avril Lavigne': [{'id': Project.objects.first().id, 'title': 'Girlfriend'}]}],
            'Social': []
        }
        self.assertEqual(json.loads(response.content), res)

    def test_workspace_list(self):
        url = reverse('comparison:cmpr_workspaces-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)[0]['cmpr_workspace_projects']), 1)

    def test_projects_list(self):
        ws = WorkspaceComparison.objects.first()
        url = reverse('comparison:workspace_projects-list', kwargs={'workspace_pk': ws.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)[0]['cmpr_items']), 1)

    def test_projects_retrieve(self):
        ws = WorkspaceComparison.objects.first()
        pr = ProjectComparison.objects.first()
        url = reverse('comparison:workspace_projects-detail', kwargs={'workspace_pk': ws.id, 'pk': pr.id})
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)['cmpr_items']), 1)

    def test_workspace_create(self):
        dep = department.objects.first()
        data = [{
            'title': 'Workspace',
            'description': '',
            'department': dep.pk,
            'members': [],
            'comparison_projects': [{
                'title': 'project',
                'creator': 'null',
                'members': [],
                'project_type': '',
                'comparison_items': [{
                    'module_type': '',
                    'module_project_id': '',
                    'project': ''
                }]
            }],
        }]
        url = reverse('comparison:cmpr_workspaces-list')
        response = self.client.post(url, data, format='json')
        print(json.loads(response.content))
        self.assertEqual(json.loads(response.content), 1)
