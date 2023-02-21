from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from accounts.models import department

class MainFlowTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_main_flow(self):
    dep = department.objects.create(
              departmentname='TestDepartment',
              max_users=2,
              max_projects=2,
              current_number_of_projects=0,
              current_number_of_users=0
            )
    user = User.objects.create_user(username='user', password='user')
    user.user_profile.department = dep
    user.user_profile.save()
    self.client.login(username='user', password='user')
    cookie = self.client.cookies['sessionid']
    self.selenium.get(self.live_server_url + '')
    self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
    self.selenium.refresh()
    self.selenium.get('%s%s' % (self.live_server_url, '/dashboard'))
    create_workspace_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
    create_workspace_button.click()
    name = self.selenium.find_element(By. CLASS_NAME, 'input')
    name.send_keys('First Workspace')
    ws_description = self.selenium.find_element(By. CLASS_NAME, 'textarea')
    ws_description.send_keys('Short description')
    next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    next_button.click()
    project_name = self.selenium.find_element(By. CLASS_NAME, 'input')
    project_name.send_keys('First Project')
    pr_description = self.selenium.find_element(By. CLASS_NAME, 'textarea')
    pr_description.send_keys('Pr. description')
    #online_checkbox = self.selenium.find_elements(By. CLASS_NAME, 'radio-description')
    #online_checkbox[1].click()
    next_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
    next_button.click()
    create_pr_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
    create_pr_button.click()
    assert 'Define the search' in self.selenium.page_source
    self.selenium.close()
