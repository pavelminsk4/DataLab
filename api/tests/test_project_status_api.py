from common.factories.project import ProjectFactory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from project.models import Project
from unittest.mock import patch
import json


class ProjectStatusTests(APITestCase):

    @patch('api.services.stop_livestream_service.StopLivestreamService.execute', return_value=True)
    def test_changing_project_status(self, stop_livestream):
        user = User.objects.create(username='MiskKSA')
        self.client.force_login(user)

        pr = ProjectFactory(
            title='Project1',
            keywords=['Keyword'],
            start_search_date='2022-10-10T00:00:00Z',
            end_search_date='2022-10-16T00:00:00Z',
            creator=user
        )

        self.client.patch(f'/api/project_statuses/{pr.id}/', {'status': 'inactive'}, format='json')
        stop_livestream.assert_called_with(pr.id)

        self.assertEqual(Project.objects.get(pk=pr.id).status, Project.STATUS_INACTIVE)
