import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from Pages.PageLogin import ClassLogin
from Pages.PageTimesheet import ClassTimeSheet
from TestData.TestVariables import ClassTestVariables
import unittest


class Class_Fill_Time_Sheet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ClassTestVariables.CHROME_PATH)

    # cls.Fill_Time_Sheet(cls)
    # browser = webdriver.Chrome(ClassTestVariables.CHROME_PATH)

    def test_Fill_Time_Sheet(self):
        plogin = ClassLogin(self.driver)
        ptimesheet = ClassTimeSheet(self.driver)
        plogin.launch_entity()
        plogin.login_entity(ClassTestVariables.Username, ClassTestVariables.Password)
        ptimesheet.go_to_timesheet()
        ptimesheet.fill_timesheet()

    @classmethod
    def tearDownClass(cls):
        # plogin.logout_entity()
        pass


if __name__ == "__main__":
    unittest.main()
