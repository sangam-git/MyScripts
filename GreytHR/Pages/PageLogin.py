
from TestData import TestVariables

Variables = TestVariables.ClassTestVariables

class Locators_login:
    # for Login
    editbox_username_name = "username"
    editbox_password_name = "password"
    button_login_xpath = "//button[@type='submit']"
    webelement_login_error_xpath = "//div[contains(text(),'Seems that either username or password')]"

class Page_Login:

    def __init__(self, driver):
        # import selenium
        # from selenium import webdriver
        # self.browser = selenium.webdriver.Chrome()
        self.browser = driver

    def launch_GreytHR(self):
        print("Navigating to GreytHR and logging in")
        self.browser.get(Variables.URL)
        self.browser.set_page_load_timeout(Variables.Timeout)
        self.browser.maximize_window()
        self.browser.implicitly_wait(Variables.Timeout)

    def login_GreytHR(self, user, password):
        self.browser.find_element_by_name(Locators_login.editbox_username_name).send_keys(user)
        self.browser.find_element_by_name(Locators_login.editbox_password_name).send_keys(password)
        self.browser.find_element_by_xpath(Locators_login.button_login_xpath).click()
        # time.sleep(7)
        # if self.browser.find_element_by_name(Page_login.editbox_username_name).is_displayed():
        #     self.login_GreytHR(user, password)

    def logout_GreytHR(self):
        self.browser.close()