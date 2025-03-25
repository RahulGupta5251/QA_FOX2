from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class Loginpage(Basepage):
    def __init__(self,driver):
        super().__init__(driver)

    email_address_field_xpath = "//*[@id='input-email']"
    password_field_xpath = "//*[@name='password']"
    login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input"
    warning_error_msg_xpath = "//div[@class = 'alert alert-danger alert-dismissible']"


    def enter_email_address(self,email_value):
        self.type_on_element(email_value,"email_address_field_xpath",self.email_address_field_xpath,)
        # self.driver.find_element(By.XPATH,self.email_address_field_xpath).send_keys(email_value)


    def enter_password(self, password_value):
        self.type_on_element(password_value,"password_field_xpath",self.password_field_xpath)
        # self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_value)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()


    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_error_msg_xpath).text
    def enter_login_to_application_credentials(self,email_value,password_value):
        self.enter_email_address(email_value)
        self.enter_password(password_value)
        self.click_on_login_button()
