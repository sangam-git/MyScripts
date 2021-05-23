import time

from selenium.webdriver.support.select import Select
from Locators.Locators import Loc_TimeSheet
from TestData.TestVariables import ClassTestVariables
import js2py

ClassTestVariables = ClassTestVariables


class ClassTimeSheet:
    def __init__(self, driver):
        self.browser = driver

    def go_to_timesheet(self):
        self.browser.find_element_by_id(Loc_TimeSheet.link_nTrack).click()
        self.browser.find_element_by_link_text(Loc_TimeSheet.link_project).click()
        self.browser.find_element_by_link_text(Loc_TimeSheet.link_timesheet).click()

    def fill_timesheet(self):
        if ClassTestVariables.TaskType == "Daily":
            self.browser.find_element_by_name(Loc_TimeSheet.radiobutton_tasktype).click()
        else:
            self.browser.find_element_by_name(Loc_TimeSheet.radiobutton_tasktype).click()

        # add a date picker here with Java Script
        time.sleep(10)
        self.browser.find_element_by_xpath("//table[@id='Table2']//img[@src='images/calendar.gif']").click()
        time.sleep(2)
        js2py.EvalJs("document.fSetDate(2021,5,18,true,event)")
        self.browser.find_element_by_name(Loc_TimeSheet.editbox_task).send_keys(ClassTestVariables.Task)
        # Project code
        sel = Select(self.browser.find_element_by_xpath(Loc_TimeSheet.dropdown_projectcode))  # select by
        # select_by_visible_text() method
        sel.select_by_value(ClassTestVariables.Project)

        # self.browser.find_element_by_xpath("//select[@name='cboActivity']//option[text()='" + value + "']").click()
        sel = Select(self.browser.find_element_by_xpath(Loc_TimeSheet.dropdown_activity))  # select by
        # select_by_visible_text() method
        sel.select_by_visible_text(ClassTestVariables.Activity)

        self.browser.find_element_by_name(Loc_TimeSheet.EditBox_Comments).send_keys(ClassTestVariables.Comments)

        self.browser.find_element_by_name(Loc_TimeSheet.EditBox_EstimatedEffort).send_keys(
            ClassTestVariables.EstimatedEfforts)

        self.browser.find_element_by_name(Loc_TimeSheet.EditBox_Effort).send_keys(ClassTestVariables.Efforts)
        # CLick Submit
        # self.browser.find_element_by_name(Loc_TimeSheet.Button_Submit).click()
        # if you are trying to log extra then do not
        if self.browser.find_element_by_xpath(Loc_TimeSheet.Button_Cancel_extra_hours).is_displayed():
            self.browser.find_element_by_xpath(Loc_TimeSheet.Button_Cancel_extra_hours).click()
            print("extra hours. so pressed cancel")
