from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from common.factories.tweet_binder_post import TweetBinderPostFactory
from common.factories.workspace_social import WorkspaceSocialFactory
from common.factories.project_social import ProjectSocialFactory
from common.factories.department import DepartmentFactory
from project_social.models import ChangingTweetbinderSentiment
from django.contrib.auth.models import User
from accounts.models import Profile

from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class ChangeSentimentTests(StaticLiveServerTestCase):
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

    def test_change_sentiment(self):
        dep = DepartmentFactory()
        user = User.objects.create_user(username='user', password='user')

        user.user_profile.department = dep
        user.user_profile.role = Profile.REGULAR_USER
        user.user_profile.save()

        ws = WorkspaceSocialFactory(title='Sensika', department=dep)
        ws.members.add(user)

        p = TweetBinderPostFactory()

        pr = ProjectSocialFactory(title='Sentiment')
        ws.social_workspace_projects.add(pr)
  
        self.driver.get(self.live_server_url + '')
        self.driver.find_element(By.ID, 'id_username').send_keys('user')
        self.driver.find_element(By.ID, 'id_password').send_keys('user')
        self.driver.find_element(By.CLASS_NAME, 'login-button').click()

        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Social Media"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h3[text()="Sensika"]'))).click()
        self.wait.until(expect.presence_of_element_located((By.XPATH, '//h1[text()="Sensika"]')))
        self.driver.find_element(By.CLASS_NAME, 'td_name').click()
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//span[text()="Neutral"]'))).click()
        self.wait.until(expect.element_to_be_clickable((By.XPATH, '//span[text()="Negative"]'))).click()

        time.sleep(0.5)
        res = ChangingTweetbinderSentiment.objects.all().first()
        self.assertEqual(ChangingTweetbinderSentiment.objects.all().count(), 1)
        self.assertEqual(res.sentiment, 'negative')
        self.assertEqual(res.post.id, p.id)
        self.assertEqual(res.department.id, dep.id)
