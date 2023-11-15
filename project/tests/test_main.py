from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from accounts.models import Department
from project.models import Workspace
from unittest import skip
import time


class LoginTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.selenium = WebDriver(chrome_options=chrome_options)

    @skip('Selenium')
    def test_log_in(self):
        User.objects.create_user(username='admin', password='admin')
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        assert 'Log in' in self.selenium.page_source
        user_name = self.selenium.find_element('id', 'id_username')
        password = self.selenium.find_element('id', 'id_password')
        button = self.selenium.find_element(By. CLASS_NAME, 'login-button')
        user_name.send_keys('admin')
        password.send_keys('admin')
        button.click()
        assert 'Hello' in self.selenium.page_source
        self.selenium.close()


class WorkspaceTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.selenium = WebDriver(chrome_options=chrome_options)

    @skip('Selenium')
    def test_dashboard(self):
        dep = Department.objects.create(
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
        self.client.login(username='admin', password='admin')
        cookie = self.client.cookies['sessionid']
        self.selenium.get(self.live_server_url + '')
        self.selenium.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.selenium.refresh()
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        assert 'Hello,' in self.selenium.page_source
        module_card_main = self.selenium.find_element(By. CLASS_NAME, 'module-card')
        module_card_main.click()
        time.sleep(1)
        assert 'workspace3' not in self.selenium.page_source
        assert 'workspace1' in self.selenium.page_source
        assert 'workspace2' in self.selenium.page_source
        self.selenium.close()
