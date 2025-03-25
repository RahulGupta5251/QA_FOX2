import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.Homepage import Homepage
from pages.Registerpage import Registerpage


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class Test_register:

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "rahul"+time_stamp+"@gmail.com"

    def test_register_with_mandatory_fields(self):
        home_page = Homepage(self.driver)
        home_page.click_on_my_account_drop_menu()

        register_page = home_page.select_register_option()
        register_page.register_an_account("Rahul......","Gupta....",self.generate_email_with_time_stamp(),"7011996353","Samsung@135","Samsung@135",yes_or_no='yes',privacy_policy='select')

        # register_page.enter_first_name("Rahul......")
        # register_page.enter_last_name("Gupta....")
        # register_page.enter_telephone_number("7011996353")
        # register_page.enter_email_address(self.generate_email_with_time_stamp())
        # register_page.enter_password("Samsung@135")
        # register_page.enter_confirm_password("Samsung@135")
        # register_page.select_agree_checkbox_field()
        # register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Register").click()
        # self.driver.find_element(By.XPATH,"//*[@id='input-firstname']").send_keys("Rahul......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-lastname']").send_keys("Gupta......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-email']").send_keys(self.generate_email_with_time_stamp())
        # self.driver.find_element(By.XPATH,"//*[@id='input-telephone']").send_keys("7011996353")
        # self.driver.find_element(By.XPATH,"//*[@id='input-password']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='input-confirm']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[1]").click()###  agree_checkbox_xpath
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[2]").click()## continue
        expected_success_created_msg = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//*[@id='content']/h1").text.__eq__(expected_success_created_msg)


    def test_register_with_all_fields(self):
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Rahul......","Gupta....",self.generate_email_with_time_stamp(),"7011996353","Samsung@135","Samsung@135",yes_or_no='yes',privacy_policy='select')

        # register_page.enter_first_name("Rahul......")
        # register_page.enter_last_name("Gupta....")
        # register_page.enter_telephone_number("7011996353")
        # register_page.enter_email_address(self.generate_email_with_time_stamp())
        # register_page.enter_password("Samsung@135")
        # register_page.enter_confirm_password("Samsung@135")
        # register_page.click_yes_radio_button()
        # register_page.select_agree_checkbox_field()
        # register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Register").click()
        # self.driver.find_element(By.XPATH,"//*[@id='input-firstname']").send_keys("Rahul......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-lastname']").send_keys("Gupta......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-email']").send_keys(self.generate_email_with_time_stamp())
        # self.driver.find_element(By.XPATH,"//*[@id='input-telephone']").send_keys("7011996353")
        # self.driver.find_element(By.XPATH,"//*[@id='input-password']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='input-confirm']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").click()
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[1]").click()###  agree_checkbox_xpath
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[2]").click()## continue
        expected_success_created_msg = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//*[@id='content']/h1").text.__eq__(expected_success_created_msg)
    def test_register_with_duplicate_email(self):
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Rahul...","Gupta....","Rahulgupta5251@gmail.com","7011996353","Samsung@135","Samsung@135","yes","select")
        # register_page.enter_first_name("Rahul......")
        # register_page.enter_last_name("Gupta....")
        # register_page.enter_telephone_number("7011996353")
        # register_page.enter_email_address("Rahulgupta5251@gmail.com")
        # register_page.enter_password("Samsung@135")
        # register_page.enter_confirm_password("Samsung@135")
        # register_page.click_yes_radio_button()
        # register_page.select_agree_checkbox_field()
        # register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT,"Register").click()
        # self.driver.find_element(By.XPATH,"//*[@id='input-firstname']").send_keys("Rahul......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-lastname']").send_keys("Gupta......")
        # self.driver.find_element(By.XPATH,"//*[@id='input-email']").send_keys("Rahulgupta5251@gmail.com")
        # self.driver.find_element(By.XPATH,"//*[@id='input-telephone']").send_keys("7011996353")
        # self.driver.find_element(By.XPATH,"//*[@id='input-password']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='input-confirm']").send_keys("Samsung@135")
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").click()
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[1]").click()###  agree_checkbox_xpath
        # self.driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[2]").click()## continue
        duplicate_email_warning_msg = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH,"//*[@id='account-register']/div[1]").text.__eq__(duplicate_email_warning_msg)

    def test_register_without_entering_any_fields(self):
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("","","","","","","yes","no")
        # register_page.enter_first_name("")
        # register_page.enter_last_name("")
        # register_page.enter_telephone_number("")
        # register_page.enter_email_address("")
        # register_page.enter_password("")
        # register_page.enter_confirm_password("")
        # register_page.click_yes_radio_button()
        # register_page.select_agree_checkbox_field()
        # register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        # self.driver.find_element(By.LINK_TEXT, "Register").click()
        # self.driver.find_element(By.XPATH, "//*[@id='input-firstname']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='input-lastname']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='input-email']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='input-telephone']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='input-password']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='input-confirm']").send_keys("")
        # self.driver.find_element(By.XPATH, "//*[@id='content']/form/div/div/input[2]").click()  ## continue

        expected_first_name_warning_msg = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//*[@id='input-firstname']/following-sibling::div[1]").text.__eq__(expected_first_name_warning_msg)

        expected_last_name_warning_msg = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//*[@id='input-lastname']/following-sibling::div[1]").text.__eq__(expected_last_name_warning_msg)

        expected_email_warning_msg = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH,"//*[@id='input-email']/following-sibling::div[1]").text.__eq__(expected_email_warning_msg)

        expected_telephone_warning_msg = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//*[@id='input-telephone']//following-sibling::div[1]").text.__eq__(expected_telephone_warning_msg)

        expected_password_warning_msg = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH,"//*[@id='input-password']/following-sibling::div[1]").text.__eq__(expected_password_warning_msg)