from project_social.models import *
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from project_social.models import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pathlib import Path
import os
import environ

from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

base_url = env('APP_URL')
storage_folder = 'reports/temp/'

def prepare_social_widget_images(item):
  soc_pr = ProjectSocial.objects.get(id = item.module_project_id)
  driver = run_chrome_driver()
  screenshot_list = {}
  if item.soc_summary:
    screenshot_list.append(screen_summary(driver, soc_pr.pk))
  if item.soc_top_locations:
    screenshot_list['top_locations'] = screen_top_locations(driver, soc_pr.pk)
  if item.soc_top_authors:
    screenshot_list['top_authors'] = screen_top_authors(driver, soc_pr.pk)
  return screenshot_list

def run_chrome_driver():
  chrome_options = FirefoxOptions()
  chrome_options.add_argument("--headless")
  driver = webdriver.Firefox(
      options=chrome_options,
      service=FirefoxService(GeckoDriverManager().install())
    )
  username='admin2'
  password='anadeakey'
  driver.get(base_url)
  driver.find_element("id", "id_username").send_keys(username)
  driver.find_element("id", "id_password").send_keys(password)
  driver.find_element(By. CLASS_NAME, "login-button").click()
  return driver

def screen_summary(driver, proj_pk):
  url = base_url + "/api/reports/0/social/summary_screenshot/" + str(proj_pk) + "/"
  driver.get(url)
  time.sleep(1)
  screenshot_path = storage_folder + 'social_summary_' + str(uuid4()) + '.png'
  driver.save_screenshot(screenshot_path)
  return screenshot_path

def screen_top_locations(driver, proj_pk):
  url = base_url + "/api/reports/0/social/top_locations_screenshot/" + str(proj_pk) + "/"
  driver.get(url)
  time.sleep(1)
  screenshot_path = storage_folder + 'social_top_locations_' + str(uuid4()) + '.png'
  driver.save_screenshot(screenshot_path)
  return screenshot_path

def screen_top_authors(driver, proj_pk):
  url = base_url + "/api/reports/0/social/top_authors_screenshot/" + str(proj_pk) + "/"
  driver.get(url)
  time.sleep(1)
  screenshot_path = storage_folder + 'social_top_authors_' + str(uuid4()) + '.png'
  driver.save_screenshot(screenshot_path)
  return screenshot_path
