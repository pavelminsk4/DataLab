from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from project.models import Workspace
import time

class CreateProjectTests(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls.selenium = WebDriver()

  def test_create_project_from_existing_workspace(self):
    user = User.objects.create_user(username='user', password='user')
    ws = Workspace.objects.create(title='Sensika')
    ws.members.add(user)
    self.client.login(username='user', password='user')
    cookie = self.client.cookies['sessionid']
    self.selenium.get(self.live_server_url + '')
    self.selenium.add_cookie({'name':'sessionid', 'value':cookie.value, 'secure':False, 'path':'/'})
    self.selenium.refresh()
    self.selenium.get(self.live_server_url + '/workspace/' + str(ws.id))
    create_project_button = self.selenium.find_element(By. CLASS_NAME, 'create-new-button')
    create_project_button.click()
    next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    self.assertEqual(next_button.is_enabled(), False)
    project_name_field = self.selenium.find_element(By. CLASS_NAME, 'input')
    project_name_field.send_keys('Saudi Arabia')
    self.assertEqual(next_button.is_enabled(), False)
    online_checkbox = self.selenium.find_element(By. XPATH, "//div[contains(text(), 'Twitter and news')]")
    online_checkbox.click()
    self.assertEqual(next_button.is_enabled(), True)
    next_button.click()
    keywords_field = self.selenium.find_element(By. CLASS_NAME, "input[placeholder='Enter main keywords']")
    keywords_field.send_keys('Apple')
    keywords_field.send_keys(Keys.ENTER)
    next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
    next_button.click()
    time.sleep(1)
    assert 'Search by keywords and phrases' in self.selenium.page_source
    assert 'Back' in self.selenium.page_source
    assert 'Saudi Arabia' in self.selenium.page_source
    self.selenium.close()
