import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.common import Common
from locator.Locator import *
from utils.Environment import Environment as Env

from selenium.webdriver.common.keys import Keys
import allure



class Demo:

    @allure.step("Open url")
    def url_hit(self, url, driver):
        Common.get_url(self, driver, url)

    @allure.step("Wait for Login Element")
    def wait_for_login_element(self, driver):
        Common.wait_for_element(self, driver, LocateElement.UsernameInput, "wait for login page",
                                wait_time=10)

    @allure.step("Enter username & password ")
    def enter_username_password(self, username, password, driver):
        Common.send_text(self, driver, LocateElement.UsernameInput, username, "login ID enter")
        Common.send_text(self, driver, LocateElement.UserPass, password, "login pass enter")
        time.sleep(3)
        Common.click(self,driver,LocateElement.LoginButton,"login button")
        time.sleep(10)

    @allure.step("check out detail")
    def chekout_detail(self, name, lastname,postalcode, driver):
        Common.send_text(self, driver, LocateElement.Name, name, "Name enter")
        Common.send_text(self, driver, LocateElement.LastName, lastname, "login pass enter")
        Common.send_text(self, driver, LocateElement.PostalCode, postalcode, "login pass enter")
        time.sleep(3)
        Common.click(self, driver, LocateElement.Continue, "Continue button")
        time.sleep(10)

    @allure.step("Open cart")
    def open_cart(self, driver):
        Common.click(self,driver,LocateElement.GotoCart,"go to cart")
        time.sleep(4)

    @allure.step("dmp login test case A")
    def dmp_test_case_a(self, url,username,password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self,driver)
        Demo.enter_username_password(self,username,password,driver)
        if(len(Common.get_element(self,driver,LocateElement.AfterLoginText,"After Login check",multiple=True))>0 and len(Common.get_element(self,driver,LocateElement.Cart,"cart logo",multiple=True))>0):
            print("Login Successfull : Pass")
        else:
            print("Login Unsucessfull")
            Common.failure_screenshot(self, driver, "DMP Test Case A Login with valid cred")
            pytest.fail("Login Unsuccessfull")

    @allure.step("dmp login test case B")
    def dmp_test_case_b(self, url, username, password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        if (len(Common.get_element(self, driver, LocateElement.AfterLoginText, "After Login check",
                                   multiple=True)) <= 0 and len(
                Common.get_element(self, driver, LocateElement.ErrorMessage, "cart logo", multiple=True)) > 0):
            print("Login Unsuccessfull : Pass")
        else:
            print("Login Sucessfull")
            Common.failure_screenshot(self, driver, "DMP Test Case B Login with valid username invalid password")
            pytest.fail("Login Successfull")

    @allure.step("dmp login test case C")
    def dmp_test_case_c(self, url, username, password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        if (len(Common.get_element(self, driver, LocateElement.AfterLoginText, "After Login check",
                                   multiple=True)) <= 0 and len(
            Common.get_element(self, driver, LocateElement.ErrorMessage, "cart logo", multiple=True)) > 0):
            print("Login Unsuccessfull : Pass")
        else:
            print("Login Sucessfull")
            Common.failure_screenshot(self, driver, "DMP Test Case C Login with invalid username valid password")
            pytest.fail("Login Successfull")

    @allure.step("dmp login test case D")
    def dmp_test_case_d(self, url, username, password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        Common.click(self,driver,LocateElement.OpenMenu,"Open Menu")
        time.sleep(2)
        Common.click(self,driver,LocateElement.LogoutButton,"Log out")
        time.sleep(4)
        if(len(Common.get_element(self,driver,LocateElement.UsernameInput,"Login page",multiple=True))>0 and len(Common.get_element(self,driver,LocateElement.UserPass,"Login Page",multiple=True))>0):
            print("Logout Successfull : Pass")
        else:
            print("Logout Unucessfull")
            Common.failure_screenshot(self, driver, "DMP Test Case D Logout Functionality")
            pytest.fail("Logout Unsuccessfull")

    @allure.step("dmp login test case E")
    def dmp_test_case_e(self, url, username, password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        Common.click(self,driver,LocateElement.Addtocart,"add to cart")
        time.sleep(3)
        if(len(Common.get_element(self,driver,LocateElement.CartItem,"cart count",multiple=True))>0):
            print("1 Item count Showing in Cart Logo : Pass")
            Demo.open_cart(self,driver)
            if(len(Common.get_element(self,driver,LocateElement.ItemInCart,"cart item",multiple=True))>0):
                print("Item Dispalyed in Cart : Pass")
            else:
                print("Item Not Displayed in Cart : Fail")
                Common.failure_screenshot(self, driver, "DMP Test Case E Item Not Displayed in Cart")
                pytest.fail("Item Not Displayed in Cart : Fail")
        else:
            print("1 Item count Showing in Cart Logo : Fail")
            Common.failure_screenshot(self, driver, "DMP Test Case E Cart item Count in Cart logo")
            pytest.fail("1 Item count Showing in Cart Logo : Fail")

    @allure.step("dmp login test case F")
    def dmp_test_case_f(self, url, username, password, driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        Common.click(self, driver, LocateElement.Addtocart, "add to cart")
        time.sleep(3)
        Demo.open_cart(self, driver)
        Common.click(self,driver,LocateElement.RemoveItem,"Reomve Item")
        time.sleep(3)
        if (len(Common.get_element(self, driver, LocateElement.ItemInCart, "cart item", multiple=True)) <= 0):
            print("Item not Dispalyed in Cart : Pass")
        else:
            print("Item Displayed in Cart : Fail")
            Common.failure_screenshot(self, driver, "DMP Test Case F Item Not Displayed in Cart")
            pytest.fail("Item Displayed in Cart : Fail")

    @allure.step("dmp login test case G")
    def dmp_test_case_g(self, url, username, password,name,lastname,postalcode,driver):
        Demo.url_hit(self, url, driver)
        Demo.wait_for_login_element(self, driver)
        Demo.enter_username_password(self, username, password, driver)
        Common.click(self, driver, LocateElement.Addtocart, "add to cart")
        time.sleep(3)
        Demo.open_cart(self, driver)
        Common.click(self,driver,LocateElement.Checkout,"check out")
        time.sleep(3)
        Demo.chekout_detail(self,name,lastname,postalcode,driver)
        if(len(Common.get_element(self,driver,LocateElement.PaymentInfo,"check info",multiple=True))>0 and len(Common.get_element(self,driver,LocateElement.Bill,"bill amount",multiple=True))>0):
            print("Shipping Info and Bill Amount Displayed : Pass")
            Common.scroll_into_view(self,driver,LocateElement.Finish,"scorll")
            time.sleep(4)
            Common.click(self,driver,LocateElement.Finish,"Finish")
            time.sleep(4)
            if(len(Common.get_element(self,driver,LocateElement.SuccessCheckout,"success",multiple=True))>0 and len(Common.get_element(self,driver,LocateElement.OrderSuccess,"check",multiple=True))>0):
                print("Order Placed : Pass")
            else:
                print("Order not Placed : Fail")
                Common.failure_screenshot(self, driver, "DMP Test Case G order not placed")
                pytest.fail("Order not Placed : Fail")
        else:
            print("Shipping Info and Bill Amount not Displayed : Fail")
            Common.failure_screenshot(self, driver, "DMP Test Case G Shipping info and bill amount")
            pytest.fail("Shipping Info and Bill Amount not Displayed : Fail")







