from django.test import TestCase
from common.factories.project import ProjectFactory
from project.models import Project
from project.tasks.run_livesearch import run_livesearch
from unittest.mock import patch


class RunLivesearchTestCase(TestCase):
    @patch('talkwalker.classes.livestream.Livestream.__init__', return_value=None)
    def test_livesearch_for_inactive_projects(self, livestream):
        """Livesearch does not check updates for inactive and collecting projects"""
        ProjectFactory(status=Project.STATUS_COLLECTING, sources=['talkwalker'])
        ProjectFactory(status=Project.STATUS_INACTIVE, sources=['talkwalker'])

        run_livesearch()
        livestream.assert_not_called()

    @patch('talkwalker.classes.livestream.Livestream.read', return_value=True)
    @patch('talkwalker.classes.livestream.Livestream.__init__', return_value=None)
    def test_livesearch_for_active_projects(self, livestream, read):
        """Livesearch checks updates for active projects"""
        project = ProjectFactory(status=Project.STATUS_ACTIVE, sources=['talkwalker'])

        run_livesearch()
        livestream.assert_called_with(project.id, 'Project')
        read.assert_called()
