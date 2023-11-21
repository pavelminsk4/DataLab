from common.factories.project import ProjectFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from project.models import Project
from unittest.mock import patch
import json


class ProjectStatusTests(APITestCase):

    @patch('talkwalker.classes.livestream.Livestream.delete', return_value=True)
    @patch('talkwalker.classes.livestream.Livestream.__init__', return_value=None)
    def test_changing_project_status(self, livestream, delete):
        user = User.objects.create(username='MiskKSA')
        self.client.force_login(user)

        project = ProjectFactory(
            title='Project1',
            keywords=['Keyword'],
            start_search_date='2022-10-10T00:00:00Z',
            end_search_date='2022-10-16T00:00:00Z',
            creator=user
        )

        self.client.patch(f'/api/project_statuses/{project.id}/', {'status': 'inactive'}, format='json')
        livestream.assert_called_with(project.id, 'Project')
        delete.assert_called()

        self.assertEqual(Project.objects.get(id=project.id).status, Project.STATUS_INACTIVE)
