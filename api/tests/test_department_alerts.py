from rest_framework.test import APITestCase
from rest_framework import status
from alerts.models import Alert, AlertItem
from accounts.models import department
from project.models import Project
from project_social.models import ProjectSocial
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
import json

class DepartmentAlertsTests(APITestCase):
  def test_department_alerts_endpoint(self):
    dep1 = department.objects.create(departmentname='First Dep')
    dep2 = department.objects.create(departmentname='Second Dep')
    user = User.objects.create_user(id=1, username='user')
    pr = Project.objects.create(
        title='ProjectFirst',
        keywords=['Keyword'],
        additional_keywords=[],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user,
      )
    pr_soc = ProjectSocial.objects.create(
        title='ProjectSecond',
        keywords=['Keyword'],
        start_search_date=datetime(2022, 10, 10),
        end_search_date=datetime(2022, 10, 16),
        creator=user,
      )
    item1 = AlertItem.objects.create(
      module_type='Project',
      module_project_id=pr.id,
      previous_posts_count=0,
    )
    item2 = AlertItem.objects.create(
      module_type='ProjectSocial',
      module_project_id=pr_soc.id,
      previous_posts_count=0,
    )
    a1 = Alert.objects.create(
        title='First Alert',
        department=dep1,
      )
    a1.items.set([item1, item2])
    a2 = Alert.objects.create(
        title='Test Alert',
        department=dep2,
      )
    a3 = Alert.objects.create(
        title='Weekly Alert',
        department=dep2,
      )
    a4 = Alert.objects.create(
        title='Hourly Alert',
        department=dep2,
      )
    url = reverse('dep_alerts', kwargs={'pk':dep1.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    res = [
      {
        'id': a1.pk,
        'title': 'First Alert',
        'items': [item1.id, item2.id],
        'creator': None,
        'department': dep1.id,
        'project': None,
        'user': [],
        'triggered_on_every_n_new_posts': 1,
        'how_many_posts_to_send': 1,
        'alert_condition': None,
        'updated_at': a1.updated_at.replace(tzinfo=None).isoformat() + 'Z',
        'created_at': a1.created_at.replace(tzinfo=None).isoformat() + 'Z',
      },
    ]
    self.assertEqual(json.loads(response.content), res)
