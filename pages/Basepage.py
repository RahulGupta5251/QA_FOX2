from selenium.webdriver.common.by import By


class Basepage:
    def __init__(self,driver):
        self.driver = driver

    def type_on_element(self,text,locator_name, locator_value):
        element = self.get_element(locator_name,locator_value)
        # element = None
        # if locator_name.endswith("xpath"):
        #     element = self.driver.find_element(By.XPATH,locator_value)
        # elif locator_name.endswith("link_text"):
        #     element =self.driver.find_element(By.LINK_TEXT,locator_value)
        # elif locator_name.endswith("_id"):
        #     element =self.driver.find_element(By.ID,locator_value)
        # elif locator_name.endswith("_css_selector"):
        #     element =self.driver.find_element(By.CSS_SELECTOR,locator_value)
        # elif locator_name.endswith("_class"):
        #     element = self.driver.find_element(By.CLASS_NAME,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name, locator_value)
        # element = None
        # if locator_name.endswith("xpath"):
        #     element = self.driver.find_element(By.XPATH,locator_value)
        # elif locator_name.endswith("link_text"):
        #     element =self.driver.find_element(By.LINK_TEXT,locator_value)
        # elif locator_name.endswith("_id"):
        #     element =self.driver.find_element(By.ID,locator_value)
        # elif locator_name.endswith("_css_selector"):
        #     element =self.driver.find_element(By.CSS_SELECTOR,locator_value)
        # elif locator_name.endswith("_class"):
        #     element = self.driver.find_element(By.CLASS_NAME,locator_value)
        element.click()
    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("xpath"):
            element = self.driver.find_element(By.XPATH,locator_value)
        elif locator_name.endswith("link_text"):
            element =self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_name.endswith("_id"):
            element =self.driver.find_element(By.ID,locator_value)
        elif locator_name.endswith("_css_selector"):
            element =self.driver.find_element(By.CSS_SELECTOR,locator_value)
        elif locator_name.endswith("_class"):
            element = self.driver.find_element(By.CLASS_NAME,locator_value)
        return element

    def retrive_element_text(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        return element.text