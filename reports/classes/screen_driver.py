from time import sleep
from project_social.models import *
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from django.forms.models import model_to_dict
from functools import reduce

from pathlib import Path
import os
import environ

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

base_url = env('APP_URL')
storage_folder = 'reports/tmp/'


class ScreenDriver:
    def __init__(self, item):
        self.item = item

    def __run_chrome_driver(self):
        chrome_options = FirefoxOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Firefox(
            options=chrome_options,
            service=FirefoxService(GeckoDriverManager().install())
        )
        username = 'admin2'
        password = 'anadeakey'
        driver.set_window_size(700, 520, driver.current_window_handle)
        driver.get(base_url)
        driver.find_element('id', 'id_username').send_keys(username)
        driver.find_element('id', 'id_password').send_keys(password)
        driver.find_element(By. CLASS_NAME, 'login-button').click()
        return driver

    def __make_screenshot(self, widget, driver):
        url = f'{base_url}/api/reports/{widget}_screenshot/{str(self.item.module_project_id)}/'
        driver.get(url)
        # We must to replace sleep with it in the nearest future - WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'canvas')))
        sleep(0.5)
        screenshot_path = f'{storage_folder}{widget}_{str(uuid4())}.png'
        driver.save_screenshot(screenshot_path)
        return screenshot_path

    def __check_and_create_tmp_dir(self):
        if not os.path.exists(storage_folder):
            os.makedirs(storage_folder)

    def get_screenshots(self):
        driver = self.__run_chrome_driver()
        self.__check_and_create_tmp_dir()
        item_widgets = model_to_dict(
            self.item, exclude=['module_type', 'module_project_id', 'id'])
        return reduce(
            lambda acc, widget: {**acc, **{widget: self.__make_screenshot(widget, driver)}} if item_widgets[widget] else acc,
            item_widgets, {})
