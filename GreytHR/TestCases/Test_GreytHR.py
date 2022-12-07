import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import sys

sys.path.append("C:/Users/sangameshh/PycharmProjects/GreytHR")

# Get both pages and Locators
from Pages.PageLogin import Page_Login
from Pages.PageLogin import Locators_login
from Pages.PageLogin import *

from Pages.PageHome import *

# Get Variables needed
from TestData.TestVariables import *

# Unit test and reporting
import HtmlTestRunner
import unittest


class ClassGreyTHR(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Object to access variables
        cls.variables = ClassTestVariables()
        # Launch Browser happens here
        # cls.driver = webdriver.Chrome(cls.variables.CHROME_PATH)
        # cls.driver = driver
        # cls.Login = Page_Login(cls.driver)
        # cls.Homepage = Page_Home(cls.driver)

    def setUp(self):
        print("Opening Chrome")
        self.driver = selenium.webdriver.Chrome(self.variables.CHROME_PATH)
        self.Login = Page_Login(self.driver)
        self.Homepage = Page_Home(self.driver)

    def tearDown(self) -> None:
        print("Closing Chrome")
        self.driver.quit()

    def test_validate_invalid_login(self):
        # enter invalid user name and password
        # self.driver.get(self.variables.CHROME_PATH)
        # self.driver.find_element_by_xpath(Locators_login.editbox_password_name).send_keys('invalid')
        # self.driver.find_element_by_xpath(Locators_login.editbox_username_name).send_keys('inv%3alid')
        # self.driver.find_element_by_xpath(Locators_login.button_login_xpath).click()
        # same as
        self.Login.launch_GreytHR()
        self.Login.login_GreytHR("invalid", "invalid again")
        # now is the validation after above steps
        t = self.driver.find_element_by_xpath(Locators_login.webelement_login_error_xpath).is_displayed()
        self.assertEqual(bool(t), bool(1), "Error message for Invalid Username")

    def test_ApplyWFH(self):
        self.Login.launch_GreytHR()
        self.Login.login_GreytHR(self.variables.Username, self.variables.Password)
        # self.test_login()
        self.Homepage.fill_timesheet(self.variables.Reason, "24", "28")
        # self.Homepage.logout()
        success = self.Homepage.logout()
        self.assertEqual(bool(success), bool(1), "logout successful")

    # def test_logout(self):
    #     self.driver.quit()

    def test_login_logout(self):
        self.Login.launch_GreytHR()
        self.Login.login_GreytHR(self.variables.Username, self.variables.Password)
        isHomePageLoaded = bool(self.driver.find_element_by_xpath(Loc_Homepage.link_Leave_xpath).is_displayed())
        self.assertEqual(isHomePageLoaded, bool(1), "Home page loaded")
        success = self.Homepage.logout()
        # '' self.driver.find_element_by_xpath(Loc_Homepage.webelement_logout_success).is_displayed()
        self.assertEqual(bool(success), bool(1), "logout successful")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sangameshh/PycharmProjects/GreytHR/Results'))
    # unittest.main()
