from selenium.webdriver.common.by import By
from selenium import webdriver


class LocatorBeeline:
    URL: str = "https://prod.beeline.com/fitch/Assignments/TimeAndExpense/TimeAndExpense.aspx"
    link_login_to_beeline: tuple[By, str] = By.ID, "loginButtonLink"
    textbox_user_name: tuple[By, str] = By.ID, "username"
    button_continue: tuple[By, str] = By.XPATH, "//button[text()='Continue']"
    textbox_password: tuple[By, str] = By.ID, "password"

    @staticmethod
    def box_date(day: str):
        return By.XPATH, f"//td[@class='day']//input[starts-with(@date,'{day}')]"

    textbox_hours_active: tuple[By, str] = By.ID, "timesheetEntryControl_EntryTextBox"
    button_comment_active: tuple[By, str] = By.XPATH, ('//div[@id="timesheetEntryControl_EntryActionsContainer"]'
                                                       '//a[@title="Comments"]')
    textbox_comments: tuple[By, str] = By.ID, "timesheetEntryControl_EntryCommentTextArea"
    button_submit_timesheet: tuple[By, str] = By.ID, "submitTimesheetButton"
    button_save: tuple[By, str] = By.ID, "saveTimesheetButton"
    button_submit_for_approval : tuple[By, str] = By.XPATH, "//button[text()='Submit for Approval']"


class PageBeeline:
    """Beeline """

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Edge()
        self.driver.implicitly_wait(20)

    def login_to_beeline(self, username: str, password: str):
        self.driver.get(LocatorBeeline.URL)
        self.driver.find_element(*LocatorBeeline.link_login_to_beeline).click()
        self.driver.find_element(*LocatorBeeline.textbox_user_name).send_keys(username)
        self.driver.find_element(*LocatorBeeline.button_continue).click()
        self.driver.find_element(*LocatorBeeline.textbox_password).send_keys(password)
        self.driver.find_element(*LocatorBeeline.button_continue).click()
        if self.driver.find_element(*LocatorBeeline.button_submit_timesheet):
            print("Beeline login successful")
            return True
        else:
            print("Beeline login failed")
            return False

    def fill_hours(self, days: dict):

        for day in days:
            if self.driver.find_element(*LocatorBeeline.box_date(day)).get_attribute("disabled") == "true":
                print(f"{day} is disabled")
                continue
            self.driver.find_element(*LocatorBeeline.box_date(day)).click()
            self.driver.find_element(*LocatorBeeline.textbox_hours_active).send_keys("8")

        self.driver.find_element(*LocatorBeeline.button_save).click()
        self.driver.find_element(*LocatorBeeline.button_submit_timesheet).click()
