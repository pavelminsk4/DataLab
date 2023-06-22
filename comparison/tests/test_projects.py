from common.factories.workspace_comparison import WorkspaceComparisonFactory
from common.factories.project_comparison import ProjectComparisonFactory
from comparison.models import ProjectComparison, WorkspaceComparison
from common.factories.comparison_item import ComparisonItemFactory
from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from accounts.models import Profile, department
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
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
        wscmpr.members.set([user])
        prcmpr = ProjectComparisonFactory(workspace=wscmpr)
        prcmpr.members.set([user])
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
        pr = Project.objects.first()
        data = {
            'title': 'Workspace',
            'description': '',
            'department': dep.pk,
            'members': [],
            'cmpr_workspace_projects':[{
                    'title': 'ProjTitle',
                    'members': [],
                    'cmpr_items': [{
                        'module_type': 'Project',
                        'module_project_id': pr.id,
                    }],
                }],
        }
        url = reverse('comparison:cmpr_workspaces-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(json.loads(response.content)['cmpr_workspace_projects'][0]['title'], 'ProjTitle')

    def test_widget_list(self):
        pr = ProjectComparison.objects.first()
        self.assertEqual(pr.cmpr_widgets.get(default_title='Summary').title, 'Summary')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Content volume').title, 'Content volume')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Top authors').title, 'Top authors')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Sentiment').title, 'Sentiment')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Top sources').title, 'Top sources')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Top keywords').title, 'Top keywords')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Top languages').title, 'Top languages')
        self.assertEqual(pr.cmpr_widgets.get(default_title='Top countries').title, 'Top countries')
