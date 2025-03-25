import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.Homepage import Homepage
from pages.Loginpage import Loginpage


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class Test_login:

    def test_login_with_valid_credentials(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.enter_login_to_application_credentials("rahulgupta5251@gmail.com","Samsung@135")
        # login_page.enter_email_address("rahulgupta5251@gmail.com")
        # login_page.enter_password("Samsung@135")
        # login_page.click_on_login_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Login").click()
        # self.driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys("rahulgupta5251@gmail.com")
        # self.driver.find_element(By.XPATH,"//*[@name='password']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()
        expected_login_success_msg = "My Account"
        assert self.driver.find_element(By.XPATH,"//*[@id='content']/h2[1]").text.__eq__(expected_login_success_msg)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rahul"+time_stamp+"@gmail.com"

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.enter_login_to_application_credentials(self.generate_email_with_time_stamp(),"Samsung@135")
        # login_page.enter_email_address(self.generate_email_with_time_stamp())
        # login_page.enter_password("Samsung@135")
        # login_page.click_on_login_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Login").click()
        # self.driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys(self.generate_email_with_time_stamp())
        # self.driver.find_element(By.XPATH,"//*[@name='password']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()
        expected_login_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@class = 'alert alert-danger alert-dismissible']").text.__eq__(expected_login_warning_msg)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.enter_login_to_application_credentials("rahulgupta5251@gmail.com","12345678")
        # login_page.enter_email_address("rahulgupta5251@gmail.com")
        # login_page.enter_password("12345678")
        # login_page.click_on_login_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Login").click()
        # self.driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys("rahulgupta5251@gmail.com")
        # self.driver.find_element(By.XPATH,"//*[@name='password']").send_keys("1234567789")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()
        expected_login_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@class = 'alert alert-danger alert-dismissible']").text.__eq__(expected_login_warning_msg)
        time.sleep(2)

