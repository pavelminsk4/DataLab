from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from webdriver_manager.firefox import GeckoDriverManager
from django.forms.models import model_to_dict

from functools import reduce
from pathlib import Path
import os
import environ

from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

base_url = env('APP_URL')
storage_folder = 'reports/tmp/'


class ScreenDriver:
    def __init__(self, item):
        self.item = item

        options = FirefoxOptions()
        options.add_argument('--width=700')
        options.add_argument('--height=520')
        options.add_argument('--headless')

        self.driver = webdriver.Firefox(
            options=options,
            service=FirefoxService(GeckoDriverManager().install())
        )

        self.wait = WebDriverWait(self.driver, 10)

    def screenshot(self, widget):
        url = f'{base_url}/api/reports/{widget}_screenshot/{str(self.item.module_project_id)}/'
        screenshot_path = f'{storage_folder}{widget}_{str(uuid4())}.png'

        self.driver.get(url)
        self.wait.until(expect.presence_of_element_located((By.TAG_NAME, 'canvas')))
        self.driver.save_screenshot(screenshot_path)

        return screenshot_path

    def screenshots(self):
        if not os.path.exists(storage_folder):
            os.makedirs(storage_folder)

        widgets = model_to_dict(self.item, exclude=['module_type', 'module_project_id', 'id'])
        result  = reduce(lambda acc, w: {**acc, **{w: self.screenshot(w)}} if widgets[w] else acc, widgets, {})

        self.driver.quit()
        return result
