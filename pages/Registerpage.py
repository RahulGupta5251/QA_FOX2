from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class Registerpage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)


    first_name_field_xpath = "//*[@id='input-firstname']"
    last_name_field_xpath = "//*[@id='input-lastname']"
    email_field_xpath = "//*[@id='input-email']"
    telephone_field_xpath = "//*[@id='input-telephone']"
    password_field_xpath = "//*[@id='input-password']"
    confirm_password_field_xpath = "//*[@id='input-confirm']"

    agree_checkbox_xpath = "//*[@id='content']/form/div/div/input[1]"
    continue_button_xpath = "//*[@id='content']/form/div/div/input[2]"
    yes_radio_button_xpath = "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input"
    duplicate_email_warning_xpath = "//*[@id='account-register']/div[1]"

    first_name_warning_xpath = "//*[@id='input-firstname']/following-sibling::div[1]"
    last_name_warning_xpath= "//*[@id='input-lastname']/following-sibling::div[1]"
    email_address_warning_xpath = "//*[@id='input-email']/following-sibling::div[1]"
    telephone_warning_xpath = "//*[@id='input-telephone']//following-sibling::div[1]"
    password_warning_xpath = "//*[@id='input-password']/following-sibling::div[1]"

    def enter_first_name(self,first_name_value):
        self.type_on_element(first_name_value,"first_name_field_xpath",self.first_name_field_xpath)

        # self.driver.find_element(By.XPATH,self.first_name_field_xpath).clear()
        # self.driver.find_element(By.XPATH,self.first_name_field_xpath).click()
        # self.driver.find_element(By.XPATH,self.first_name_field_xpath).send_keys(first_name_value)

    def enter_last_name(self,last_name_value):
        self.type_on_element(last_name_value,"last_name_field_xpath",self.last_name_field_xpath)
        # self.driver.find_element(By.XPATH,self.last_name_field_xpath).clear()
        # self.driver.find_element(By.XPATH,self.last_name_field_xpath).click()
        # self.driver.find_element(By.XPATH,self.last_name_field_xpath).send_keys(last_name_value)

    def enter_email_address(self,email_value):
        self.type_on_element(email_value,"email_field_xpath",self.email_field_xpath)
        # self.driver.find_element(By.XPATH,self.email_field_xpath).clear()
        # self.driver.find_element(By.XPATH,self.email_field_xpath).click()
        # self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(email_value)

    def enter_telephone_number(self,phonenumber_value):
        self.type_on_element(phonenumber_value,"telephone_field_xpath",self.telephone_field_xpath)
        # self.driver.find_element(By.XPATH, self.telephone_field_xpath).clear()
        # self.driver.find_element(By.XPATH, self.telephone_field_xpath).click()
        # self.driver.find_element(By.XPATH, self.telephone_field_xpath).send_keys(phonenumber_value)

    def enter_password(self, password_value):
        self.type_on_element(password_value,"password_field_xpath",self.password_field_xpath)
        # self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        # self.driver.find_element(By.XPATH, self.password_field_xpath).click()
        # self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_value)

    def enter_confirm_password(self,confirm_password_value):
        self.type_on_element(confirm_password_value,"confirm_password_field_xpath",self.confirm_password_field_xpath)
        # self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).clear()
        # self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).click()
        # self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).send_keys(confirm_password_value)

    def click_yes_radio_button(self):
        self.element_click("yes_radio_button_xpath",self.yes_radio_button_xpath)
        # self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def select_agree_checkbox_field(self):
        self.element_click("agree_checkbox_xpath",self.agree_checkbox_xpath)
        # self.driver.find_element(By.XPATH, self.agree_checkbox_xpath).click()


    def click_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def register_an_account(self,first_name_value,last_name_value,email_value,phonenumber_value,password_value,confirm_password_value,yes_or_no,privacy_policy):
        self.enter_first_name(first_name_value)
        self.enter_last_name(last_name_value)
        self.enter_email_address(email_value)
        self.enter_telephone_number(phonenumber_value)
        self.enter_password(password_value)
        self.enter_confirm_password(confirm_password_value)
        if yes_or_no == "yes":
            self.click_yes_radio_button()
        if privacy_policy =="select":
            self.select_agree_checkbox_field()
        self.click_continue_button()










