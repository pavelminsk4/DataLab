
from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from common.factories.user import UserFactory
from rest_framework.test import APITestCase
from accounts.models import Profile
from project.models import Project
from rest_framework import status
from django.urls import reverse
from datetime import datetime
import json


class WorkspaceTests(APITestCase):
    def test_workspaces(self):
        user = UserFactory()
        department = DepartmentFactory()
        workspace1 = WorkspaceFactory(department=department)
        workspace1.members.add(user)
        workspace2 = WorkspaceFactory(department=department)
        workspace2.members.add(user)
        p1 = PostFactory()
        p2 = PostFactory()
        p3 = PostFactory()
        p4 = PostFactory()
        p5 = PostFactory()
        p6 = PostFactory()
        pr1 = ProjectFactory(workspace=workspace1, creator=user)
        pr2 = ProjectFactory(workspace=workspace2, creator=user)
        
        for post in (p1, p2, p3):
            pr1.posts.add(post)
        for post in (p4, p5, p6):
            pr2.posts.add(post)

        url = reverse('workspaces_list')
        self.client.force_login(user)  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res = {
            'id': workspace1.id, 
            'title': workspace1.title, 
            'description': None, 
            'members': 
                [
                    {
                        'id': user.id, 
                        'user_profile': {
                            'id': Profile.objects.get(user=user).id, 
                            'department': None, 
                            'phone': None, 
                            'jobtitle': None, 
                            'photo': None, 
                            'role': Profile.objects.get(user=user).role, 
                            'platform_language': 'English', 
                            'user': user.id
                        }, 
                        'password': '', 
                        'last_login': datetime.strftime(user.last_login, '%Y-%m-%dT%H:%M:%S.%fZ'), 
                        'is_superuser': False, 
                        'username': user.username, 
                        'first_name': '', 
                        'last_name': '', 
                        'email': '', 
                        'is_staff': False, 
                        'is_active': True, 
                        'groups': [], 
                        'user_permissions': []
                }
            ], 
            'projects': 
                [
                    {
                        'id': pr1.id, 
                        'members': [], 
                        'note': None, 
                        'title': pr1.title, 
                        'keywords': ['post', 'keyword'], 
                        'ignore_keywords': [], 
                        'additional_keywords': [], 
                        'max_items': None, 
                        'image': None, 
                        'arabic_name': None, 
                        'english_name': None, 
                        'social': False, 
                        'online': False, 
                        'premium': False, 
                        'source': 'Online', 
                        'start_search_date': pr1.start_search_date, 
                        'end_search_date': pr1.end_search_date, 
                        'report_format': 'pdf', 
                        'report_table_content': True, 
                        'report_widgets': True, 
                        'report_content': True, 
                        'report_language': 'English', 
                        'author_filter': None, 
                        'language_filter': None, 
                        'country_filter': None, 
                        'source_filter': None, 
                        'sentiment_filter': None, 
                        'author_dimensions': None, 
                        'language_dimensions': None, 
                        'country_dimensions': None, 
                        'source_dimensions': None, 
                        'sentiment_dimensions': None, 
                        'query_filter': None, 
                        'expert_mode': False, 
                        'created_at': datetime.strftime(pr1.created_at, '%Y-%m-%dT%H:%M:%S.%fZ'), 
                        'creator': user.id, 
                        'report_template': None, 
                        'workspace': workspace1.id,
                        'status': 'collecting_data',
                }
            ], 
            'created_at': datetime.strftime(workspace1.created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
        }

        self.assertEqual(json.loads(response.content)[0], res)
