from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User
from .models import Workspace

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
    assert 'Dashboard'in self.selenium.page_source
    self.selenium.close()

class WorkspaceTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_dashboard(self):
    user1 = User.objects.create_user(username='admin', password='admin')
    user2 = User.objects.create_user(username='user', password='user')
    workspace1 = Workspace.objects.create(title='workspace1')
    workspace2 = Workspace.objects.create(title='workspace2')
    workspace3 = Workspace.objects.create(title='workspace3')
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

class MainFlowTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_main_flow(self):
    User.objects.create_user(username='user', password='user')
    self.client.login(username='user', password='user')
    cookie = self.client.cookies['sessionid']
    self.selenium.get(self.live_server_url + '')
    self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    self.selenium.refresh()
    self.selenium.get('%s%s' % (self.live_server_url, '/dashboard'))
    create_workspace_button = self.selenium.find_element(By. CLASS_NAME, 'create-new-button')
    create_workspace_button.click()
    name = self.selenium.find_element(By. CLASS_NAME, 'input')
    name.send_keys('First Workspace')
    ws_description = self.selenium.find_element(By. CLASS_NAME, 'description-field')
    ws_description.send_keys('Short description')
    next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    next_button.click()
    project_name = self.selenium.find_element(By. CLASS_NAME, 'input')
    project_name.send_keys('First Project')
    pr_description = self.selenium.find_element(By. CLASS_NAME, 'description-field')
    pr_description.send_keys('Pr. description')
    online_checkbox = self.selenium.find_elements(By. CLASS_NAME, 'radio-description')
    online_checkbox[1].click()
    next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    next_button.click()
    create_pr_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    create_pr_button.click()
    assert 'First Workspace' in self.selenium.page_source
    self.selenium.close()
