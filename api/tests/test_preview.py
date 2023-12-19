from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from common.factories.workspace import WorkspaceFactory
from common.factories.feedlink import FeedlinkFactory
from selenium.webdriver.common.keys import Keys
from common.factories.post import PostFactory
from selenium.webdriver.common.by import By
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import status
from selenium import webdriver
from datetime import timedelta
import time
import json


class PreviewTests(APITestCase):
    def setUp(self):
        feedlink = FeedlinkFactory(source1='TIMES', country='USA')
        self.post1 = PostFactory(feedlink=feedlink, entry_title='USA lalalala', sentiment='positive', entry_author='BBC', entry_published=now()-timedelta(days=1))
        self.post2 = PostFactory(entry_title='Canada lalalala', entry_published=now())
        
    def test_preview(self):
        data = {
            'keywords': ['USA', 'CANADA'],
            'exclude': [],
            'additional': [],
            'country': ['USA'],
            'language': [],
            'source': ['TIMES'],
            'author': ['BBC'],
            'sentiment': ['positive']
        }
        
        url = '/api/project/preview'
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['posts'][0]['id'], self.post1.id)


class PreviewButtonTests(StaticLiveServerTestCase):
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

    def test_preview_button(self):
        user = User.objects.create_user(username='user', password='user')
        feedlink = FeedlinkFactory(source1='TIMES', country='USA')
        PostFactory(feedlink=feedlink, entry_title='USA lalalala', sentiment='positive', entry_author='BBC', entry_published=now()-timedelta(days=1))
        ws = WorkspaceFactory(title='Sensika')
        ws.members.add(user)

        self.driver.get(self.live_server_url + '')
        self.driver.find_element(By.ID, 'id_username').send_keys('user')
        self.driver.find_element(By.ID, 'id_password').send_keys('user')
        self.driver.find_element(By.CLASS_NAME, 'login-button').click()

        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Online"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Sensika"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h1[text()="Sensika"]')))

        self.driver.find_element(By.CLASS_NAME, 'base-button').click()
        time.sleep(0.5)

        self.wait.until(expect.visibility_of_element_located((By.ID, 'Name'))).send_keys('First Project')
        self.wait.until(expect.element_to_be_clickable((By.CLASS_NAME, 'next-button'))).click()
        self.wait.until(expect.visibility_of_element_located((By.CLASS_NAME, 'input[name="keywords"]'))).send_keys('USA')

        self.driver.find_element(By.CLASS_NAME, 'input[name="keywords"]').send_keys(Keys.ENTER)

        self.wait.until(expect.element_to_be_clickable((By.CLASS_NAME, 'base-button'))).click()
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//*[text()="Preview"]'))).click()

        self.wait.until(expect.presence_of_element_located((By.XPATH, '//a[text()="USA lalalala"]')))
        self.assertEqual(len(self.driver.find_elements(By.XPATH, '//a[text()="USA lalalala"]')), 1)
