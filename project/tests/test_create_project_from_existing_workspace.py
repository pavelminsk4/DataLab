from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from django.contrib.auth.models import User
from project.models import Project
from accounts.models import Profile

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class CreateProjectTests(StaticLiveServerTestCase):
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

    def test_create_project_from_existing_workspace(self):
        dep = DepartmentFactory()
        user = User.objects.create_user(username='user', password='user')

        user.user_profile.department = dep
        user.user_profile.role = Profile.ADMIN
        user.user_profile.save()

        ws = WorkspaceFactory(title='Sensika', department=dep)
        ws.members.add(user)

        self.driver.get(self.live_server_url + '')
        self.driver.find_element(By.ID, 'id_username').send_keys('user')
        self.driver.find_element(By.ID, 'id_password').send_keys('user')
        self.driver.find_element(By.CLASS_NAME, 'login-button').click()

        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()=" Online "]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Sensika"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h1[text()="Sensika"]')))

        self.driver.find_element(By.CLASS_NAME, 'base-button').click()
        time.sleep(0.5)

        self.wait.until(expect.visibility_of_element_located((By.ID, 'Name'))).send_keys('First Project')
        self.wait.until(expect.element_to_be_clickable((By.CLASS_NAME, 'next-button'))).click()
        self.wait.until(expect.visibility_of_element_located((By.CLASS_NAME, 'input[name="keywords"]'))).send_keys('Apple')

        self.driver.find_element(By.CLASS_NAME, 'input[name="keywords"]').send_keys(Keys.ENTER)
        self.wait.until(expect.element_to_be_clickable((By.NAME, 'checkbox-rss'))).click()

        self.wait.until(expect.element_to_be_clickable((By.CLASS_NAME, 'base-button'))).click()
        self.wait.until(expect.visibility_of_element_located((By.XPATH, '//*[text()="Save confirmation"]')))
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//div[text()=" Continue "]'))).click()

        self.wait.until(expect.presence_of_element_located((
            By.XPATH, '//*[text()="The data is being collected. Your project will be ready in an hour."]')
        ))

        self.assertEqual(Project.objects.all().count(), 1)
        self.assertEqual(Project.objects.all().first().sources, ['rss'])
