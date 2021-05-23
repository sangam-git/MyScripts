import selenium
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

from TestData import TestVariables
from Locators.Locators import Loc_Login

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH , "//td[@id='123']"))

Variables = TestVariables.ClassTestVariables


class ClassLogin():
    def __init__(self, driver):
        self.browser = driver

    def launch_entity(self):
        self.browser.get(Variables.URL)
        self.browser.set_page_load_timeout(Variables.Timeout)
        self.browser.maximize_window()
        self.browser.implicitly_wait(Variables.Timeout)

    def login_entity(self, user, password):
        self.browser.find_element_by_name(Loc_Login.editbox_username).send_keys(user)
        self.browser.find_element_by_name(Loc_Login.editbox_password).send_keys(password)
        self.browser.find_element_by_name(Loc_Login.button_login).click()

    def logout_entity(self):
        self.browser.close()
