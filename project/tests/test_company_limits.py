from django.test import TestCase
from accounts.models import Department
from project.models import Workspace, Project
from django.contrib.auth.models import User


class DepartmnetLimitsTestCase(TestCase):
    def setUp(self):
        dep = Department.objects.create(
            departmentname='TestDepartment',
            max_users=2,
            max_projects=2,
            current_number_of_projects=0,
            current_number_of_users=0
        )

        user1 = User.objects.create(username='Fox')
        user2 = User.objects.create(username='Jan')

        user1.user_profile.department = dep
        user2.user_profile.department = dep

        user1.user_profile.save()
        user2.user_profile.save()

        ws = Workspace.objects.create(title='TestWorkspace', department=dep)

        Project.objects.create(
            title='Project1',
            keywords=['Keyword'],
            start_search_date='2022-10-10T00:00:00Z',
            end_search_date='2022-10-16T00:00:00Z',
            creator=user1,
            workspace=ws
        ).save()

    def test_department_limints(self):
        dep = Department.objects.get(departmentname='TestDepartment')
        self.assertEqual(dep.current_number_of_projects, 2)
        self.assertEqual(dep.current_number_of_users, 2)
        User.objects.get(username='Jan').delete()
        Project.objects.get(title='Project1').delete()
        dep = Department.objects.get(departmentname='TestDepartment')
        self.assertEqual(dep.current_number_of_projects, 1)
        self.assertEqual(dep.current_number_of_users, 1)
