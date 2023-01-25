from django.test import TestCase
from accounts.models import department
from project.models import Workspace, Project
from django.contrib.auth.models import User
from datetime import datetime

class RegularReportTestCase(TestCase):
  def setUp(self):
    dep = department.objects.create(
          departmentname='TestDepartment',
          max_users=2,
          max_projects=2,
        )
    user1 = User.objects.create(username='Fox')
    user2 = User.objects.create(username='Jan')
    user3 = User.objects.create(username='Max')
    user1.user_profile.department = dep
    user2.user_profile.department = dep
    user3.user_profile.department = dep

    user1.user_profile.save()
    user2.user_profile.save()
    #user3.user_profile.save()

    ws = Workspace.objects.create(
              title='TestWorkspace',
              department=dep,
              )

    Project.objects.create(
        title='Project1',
        keywords=['Keyword'],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user1,
        workspace=ws
        )
      
    Project.objects.create(
        title='Project2',
        keywords=['Keyword'],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user1,
        workspace=ws
        )

  def test_company_limints(self):
    total_projects_number = Project.objects.all().count()
    total_users_number = User.objects.all().count()
    self.assertEqual(total_users_number, 2)
    self.assertEqual(total_projects_number, 2)
