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
import threading

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

base_url = env('APP_URL')
time_for_screenshot = env('TIME_FOR_SCREENSHOT')
time_for_response = env('TIME_FOR_RESPONSE')
storage_folder = 'reports/tmp/'


class ScreenDriver:
    def __init__(self, item):
        self.item = item
        self.res = {}

    def __run_chrome_driver(self):
        chrome_options = FirefoxOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Firefox(
            options=chrome_options,
            service=FirefoxService(GeckoDriverManager().install())
        )
        driver.set_window_size(700, 520, driver.current_window_handle)
        return driver

    def __make_screenshot(self, widget):
        driver = self.__run_chrome_driver()
        url = f'{base_url}/api/reports/{widget}_screenshot/{str(self.item.module_project_id)}/'
        driver.get(url)
        # We must to replace sleep with it in the nearest future - WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'canvas')))
        sleep(float(time_for_screenshot))
        screenshot_path = f'{storage_folder}{widget}_{str(uuid4())}.png'
        driver.save_screenshot(screenshot_path)
        self.res[widget] = screenshot_path
        driver.quit()
        return screenshot_path

    def __check_and_create_tmp_dir(self):
        if not os.path.exists(storage_folder):
            os.makedirs(storage_folder)

    def get_screenshots(self):
        self.__check_and_create_tmp_dir()
        item_widgets = model_to_dict(
            self.item, exclude=['module_type', 'module_project_id', 'id'])
        for widget in item_widgets:
            if item_widgets[widget]:
                threading.Thread(target = self.__make_screenshot, args = [widget]).start()
        sleep(float(time_for_response))
        return self.res
