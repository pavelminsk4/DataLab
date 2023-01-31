from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User
from project.models import Workspace
from accounts.models import department

class LoginTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_log_in(self):
    user1 = User.objects.create_user(username='admin', password='admin')
    self.selenium.get('%s%s' % (self.live_server_url, '/dashboard'))
    assert 'Log in' in self.selenium.page_source
    user_name = self.selenium.find_element('id', 'id_username')
    password = self.selenium.find_element('id', 'id_password')
    button = self.selenium.find_element(By. CLASS_NAME, 'login-button')
    user_name.send_keys('admin')
    password.send_keys('admin')
    button.click()
    assert 'No workspace created' in self.selenium.page_source
    self.selenium.close()

class WorkspaceTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_dashboard(self):
    dep = department.objects.create(
              departmentname='TestDepartment',
              max_users=2,
              max_projects=2,
              current_number_of_projects=0,
              current_number_of_users=0
            )

    user1 = User.objects.create_user(username='admin', password='admin')
    user1.user_profile.department = dep
    user1.user_profile.save()

    user2 = User.objects.create_user(username='user', password='user')
    user2.user_profile.department = dep
    user2.user_profile.save()
    
    workspace1 = Workspace.objects.create(title='workspace1', department=dep)
    workspace2 = Workspace.objects.create(title='workspace2', department=dep)
    workspace3 = Workspace.objects.create(title='workspace3', department=dep)
    workspace1.members.add(user1)
    workspace2.members.add(user1)
    workspace3.members.add(user2)
    login = self.client.login(username='admin', password='admin')
    cookie = self.client.cookies['sessionid']
    self.selenium.get(self.live_server_url + '')  #selenium will set cookie domain based on current page domain
    self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    self.selenium.refresh() #need to update page for logged in user
    self.selenium.get('%s%s' % (self.live_server_url, '/dashboard'))
    assert 'workspace1' and 'workspace2' in self.selenium.page_source
    assert not 'workspace3' in self.selenium.page_source
    self.selenium.close()
