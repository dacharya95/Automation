import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from base.common import Common
from Page.demo import Demo
from allure_commons.types import AttachmentType
from utils.Environment import Environment as Env
import pytest
import allure



@allure.epic("DMP Login verify with valid and Invalid entry")
@allure.feature("DMP Login feature")
class TestDemo:

    @allure.description("Verify with Valid Login Credential")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_a_login_with_valid_credential(self, driver):
        Demo.dmp_test_case_a(self,Env.pageurl,Env.userId,Env.userPass,driver)

    @allure.description("Verify with Valid Username Invalid Password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_b_login_with_valid_username_invalid_password(self, driver):
        Demo.dmp_test_case_b(self, Env.pageurl, Env.userId,'abc', driver)

    @allure.description("Verify with Invalid Username Valid Password")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_c_login_with_invalid_username_valid_password(self, driver):
        Demo.dmp_test_case_c(self, Env.pageurl,'test_test', Env.userPass, driver)

    @allure.description("Verify with Logout Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_d_logout_functionality(self, driver):
        Demo.dmp_test_case_d(self, Env.pageurl, Env.userId, Env.userPass, driver)

    @allure.description("Verify Add to Cart Functionality")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_e_add_to_cart_functionality(self, driver):
        Demo.dmp_test_case_e(self, Env.pageurl, Env.userId, Env.userPass, driver)

    @allure.description("Verify Remove Item from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_f_remove_item_from_cart(self, driver):
        Demo.dmp_test_case_f(self, Env.pageurl, Env.userId, Env.userPass, driver)

    @allure.description("Verify place order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_g_place_order(self, driver):
        Demo.dmp_test_case_g(self, Env.pageurl, Env.userId, Env.userPass,"Dwaita","Acharya","400080", driver)
