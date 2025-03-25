from selenium.webdriver.common.by import By

from pages.Basepage import Basepage
from pages.Loginpage import Loginpage
from pages.Registerpage import Registerpage


class Homepage(Basepage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_drop_menu_xpath = "//span[text() = 'My Account']"
    login_option_link_text = "Login"
    register_button_link_text = "Register"



    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_drop_menu_xpath).click()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT,self.register_button_link_text).click()
        return Registerpage(self.driver)

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_link_text).click()
        return Loginpage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()