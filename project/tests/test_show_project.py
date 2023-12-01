from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from common.factories.post import PostFactory
from django.contrib.auth.models import User
from project.models import Project
from accounts.models import Profile

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class ShowProjectTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait   = WebDriverWait(cls.driver, 30)

    def tearDown(self):
        self.driver.close()

    def test_create_project_for_regular_user(self):
        """Regular user can see a project"""
        dep = DepartmentFactory()
        user = User.objects.create_user(username='user', password='user')

        user.user_profile.department = dep
        user.user_profile.role = Profile.REGULAR_USER
        user.user_profile.save()

        ws = WorkspaceFactory(title='Sensika', department=dep)
        ws.members.add(user)

        project1 = ProjectFactory(workspace=ws, title='First Project')
        project2 = ProjectFactory(workspace=ws, title='Second Project')

        project1.posts.set([PostFactory(entry_title='First Post')])
        project2.posts.set([PostFactory(entry_title='Second Post')])

        self.driver.get(self.live_server_url + '')
        self.driver.find_element(By.ID, 'id_username').send_keys('user')
        self.driver.find_element(By.ID, 'id_password').send_keys('user')
        self.driver.find_element(By.CLASS_NAME, 'login-button').click()

        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Online"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Sensika"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h1[text()="Sensika"]')))

        self.driver.find_element(By.CLASS_NAME, 'base-button').click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//td[text()="First Project"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h1[text()="First Project"]')))

        expect.presence_of_element_located((By.XPATH, '//a[text()="First Post"]'))
        self.assertEqual(len(self.driver.find_elements(By.XPATH, '//a[text()="Second Post"]')), 0)
