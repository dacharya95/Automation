import allure
import pytest
import sys

from allure_commons.types import AttachmentType
from webdriver_manager.driver import Driver

from CommonFunctions import *
from phone_gen import PhoneNumber
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from os import path
from typing import Any, Callable, Optional
from _pytest.fixtures import SubRequest
from pytest import fixture


ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    if sys.exc_info()[0]:
        date = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        file_name = "failed screenshot" + date
        allure.attach(driver.get_screenshot_as_png(), file_name, allure.attachment_type.PNG)
        driver.quit()

    if driver is not None:
        driver.quit()


