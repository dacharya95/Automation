import inspect
import logging
from datetime import date, datetime
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoAlertPresentException
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
import allure


class Common(object):

    def click(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}
        try:
            el = driver.find_element(locator[0],locator[1])
            el.click()
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise


    def send_text(self, driver, locator, text, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0],
                          "send_text": text}

        try:
            el = driver.find_element(locator[0],locator[1])
            el.send_keys(text)
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def wait_for_element(self, driver, locator, element_name, wait_time=30):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0],
                          "wait_time": wait_time}

        try:
            WebDriverWait(driver, wait_time).until(
                EC.visibility_of_element_located(locator))
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise


    def get_element(self, driver, locator, element_name, multiple=True):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        if multiple:
            try:
                el = driver.find_elements(locator[0],locator[1])
                return el
            except:
                Common.failure_screenshot(self, driver, element_name)
                raise
        else:
            try:
                el = driver.find_element(locator[0],locator[1])
                return el
            except:
                Common.failure_screenshot(self, driver, element_name)
                raise


    def get_text(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            return el.text
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise


    def get_url(self, driver, url):
        driver.get(url)

    def scroll_using_execute_script(self, driver):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def alert_accept(self, driver):
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()


    def switch_to_default(self, driver):
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        driver.switch_to.default_content()

    def get_title(self, driver):
        return driver.title

    def get_window_size(self, driver):
        size = driver.get_window_size()
        print(size)
        return size

    def scroll_by_view(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            el.location_once_scrolled_into_view
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def scroll_into_view(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            driver.execute_script("return arguments[0].scrollIntoView(true);", el)
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def get_attribute(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            return el.get_attribute('value')
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def context_click(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            ActionChains(driver).context_click(el).perform()
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def double_click(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            ActionChains(driver).double_click(el).perform()
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def action_chain_move_to_element(self, driver, locator, element_name):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_element(locator[0],locator[1])
            ActionChains(driver).move_to_element(el).perform()
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def action_chain_move_to_element_using_list(self, driver, locator, element_name, count):
        element_detail = {"element_name": element_name, "element_locator": locator[1], "element_type": locator[0]}

        try:
            el = driver.find_elements(locator[0],locator[1])
            ActionChains(driver).move_to_element(el[count]).perform()
        except:
            Common.failure_screenshot(self, driver, element_name)
            raise

    def switch_to_frame(self, driver, framename):
        driver.switch_to.frame(framename)

    def close(self, driver):
        driver.close()

    def failure_screenshot(self, driver, name):
        element_detail = {"Screenshot_name": name}
        size = driver.get_window_size()
        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        try:
            screenshot_file_path1 = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS")))
            screenshot_file_path = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS/Screenshot")))
            screenshot_file_failure = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS/Screenshot/Failure/")))
            screenshot_date = str(
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), os.pardir,
                                 "REPORTS/Screenshot/Failure/" + datetime.now().strftime("%d-%m-%Y") + "")))
            if not os.path.exists(screenshot_file_path1):
                os.makedirs(screenshot_file_path1)
            if not os.path.exists(screenshot_file_path):
                os.makedirs(screenshot_file_path)
            if not os.path.exists(screenshot_file_failure):
                os.makedirs(screenshot_file_failure)
            if not os.path.exists(screenshot_date):
                os.makedirs(screenshot_date)
            dt = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
            imgname = name + "_" + dt
            driver.get_screenshot_as_file(screenshot_date + "/" + imgname + ".png")
            allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
        except:
            raise

    def success_screenshot(self, driver, name):
        element_detail = {"Screenshot_name": name}
        size = driver.get_window_size()
        print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
        try:
            screenshot_file_path1 = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS/")))
            screenshot_file_path = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS/Screenshot")))
            screenshot_file_pass = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "REPORTS/Screenshot/Success/")))
            screenshot_date = str(
                os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,
                                             "REPORTS/Screenshot/Success/" + datetime.now().strftime("%d-%m-%Y") + "")))
            if not os.path.exists(screenshot_file_path1):
                os.makedirs(screenshot_file_path1)
            if not os.path.exists(screenshot_file_path):
                os.makedirs(screenshot_file_path)
            if not os.path.exists(screenshot_file_pass):
                os.makedirs(screenshot_file_pass)
            if not os.path.exists(screenshot_date):
                os.makedirs(screenshot_date)
            dt = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
            imgname = name + "_" + dt
            driver.get_screenshot_as_file(screenshot_date + "/" + imgname + ".png")
            allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
        except:
            raise
