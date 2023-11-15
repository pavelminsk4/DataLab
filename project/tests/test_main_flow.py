from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from accounts.models import Department
from unittest import skip


class MainFlowTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.selenium = WebDriver(chrome_options=chrome_options)

    @skip('Selenium')
    def test_main_flow(self):
        dep = Department.objects.create(
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
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        module_card_main = self.selenium.find_element(By. CLASS_NAME, 'module-card')
        module_card_main.click()
        create_ws_button = self.selenium.find_element(By. CLASS_NAME, 'disabled-creation')
        create_ws_button.click()
        ws_description = self.selenium.find_element(By. ID, 'Name')
        ws_description.send_keys('Short description')
        next_button = self.selenium.find_element(By. CLASS_NAME, 'next-button')
        next_button.click()
        project_name = self.selenium.find_element(By. CLASS_NAME, 'input')
        project_name.send_keys('First Project')
        next_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
        next_button.click()
        create_pr_button = self.selenium.find_element(By. CLASS_NAME, 'base-button')
        create_pr_button.click()
        assert 'Define the search' in self.selenium.page_source
        self.selenium.close()
