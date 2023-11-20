from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from common.factories.expert_filters.preset import PresetFactory
from common.factories.expert_filters.group import GroupFactory
from common.factories.department import DepartmentFactory
from common.factories.workspace import WorkspaceFactory
from common.factories.project import ProjectFactory
from django.contrib.auth.models import User
from accounts.models import Profile
from project.models import Project

from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class ApplyPresetTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        cls.driver = webdriver.Chrome(options=options)
        cls.wait   = WebDriverWait(cls.driver, 20)

    def tearDown(self):
        self.driver.close()

    def test_apply_preset_to_project(self):
        dep = DepartmentFactory()
        user = User.objects.create_user(username='user', password='user')

        user.user_profile.department = dep
        user.user_profile.role = Profile.ADMIN
        user.user_profile.save()

        ws = WorkspaceFactory(title='Sensika', department=dep)
        ws.members.add(user)

        pr = ProjectFactory()
        ws.projects.set([pr])

        g = GroupFactory(creator=user)
        ps = PresetFactory(creator=user, query=['Post AND red'])
        g.presets.set([ps])

        self.driver.get(self.live_server_url + '')
        self.driver.find_element(By.ID, 'id_username').send_keys('user')
        self.driver.find_element(By.ID, 'id_password').send_keys('user')
        self.driver.find_element(By.CLASS_NAME, 'login-button').click()
        time.sleep(0.5)

        self.driver.get(self.live_server_url + f'/online-module/workspace/{ws.id}/project/{pr.id}/dashboard')
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//div[text()=" Expert Filter"]'))).click()
        self.wait.until(expect.element_to_be_clickable((By.CLASS_NAME, 'checkmark'))).click()
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//div[text()=" Add Filter "]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, f'//*[text()="{ps.title}"]')))
        time.sleep(0.5)

        self.assertEqual(Project.objects.first().expert_presets.all().count(), 1)
