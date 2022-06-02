import os
import unittest
import time
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoAlertPresentException

from base.common import Common


class Action(unittest.TestCase):

    def __init__(self, driver: webdriver.Remote):
        super().__init__()
        self.driver = driver

    def screenshot(self):
        screenshot_file_path = './Screenshot/'
        if not os.path.exists(screenshot_file_path):
            os.makedirs(screenshot_file_path)
        dt = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
        imgname = self._testMethodName + "_" + dt
        self.driver.get_screenshot_as_file("./Screenshot/" + imgname + ".png")



