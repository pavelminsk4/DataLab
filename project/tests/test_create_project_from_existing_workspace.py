from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
import time
from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory


class CreateProjectTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

    def test_create_project_from_existing_workspace(self):
        dep = DepartmentFactory()
        user = User.objects.create_user(username='user', password='user')
        user.user_profile.department = dep
        user.user_profile.save()
        ws = WorkspaceFactory(title='Sensika', department=dep)
        ws.members.add(user)
        self.client.login(username='user', password='user')
        cookie = self.client.cookies['sessionid']
        self.selenium.get(self.live_server_url + '')
        self.selenium.add_cookie(
            {'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.selenium.refresh()
        self.selenium.get(self.live_server_url + '/online-module/workspace/' + str(ws.id))
        create_project_button = self.selenium.find_element(
            By. CLASS_NAME, 'base-button')
        create_project_button.click()
        next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
        next_button.click()
        project_name = self.selenium.find_element(By. CLASS_NAME, 'input')
        project_name.send_keys('First Project')
        next_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
        next_button.click()
        keywords_field = self.selenium.find_element(
            By. CLASS_NAME, "input[name='keywords']")
        keywords_field.send_keys('Apple')
        keywords_field.send_keys(Keys.ENTER)
        next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
        next_button.click()
        time.sleep(1)
        assert 'Download Report' in self.selenium.page_source
        assert 'Back to workspace' in self.selenium.page_source
        self.selenium.close()
