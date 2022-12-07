from selenium.webdriver.support.select import Select

# from Locators.GreytHRLocators import Loc_Homepage
# from TestData.TestVariables import ClassTestVariables
from selenium.webdriver.support.ui import Select
# ClassTestVariables = ClassTestVariables



class Loc_Homepage:
    link_Leave_xpath = "//span[text()='Leave']"
    link_My_Leave_xpath = "//span[text()='My Leave']"
    dropdownToClick_leave_type_xpath = "//gt-select-box[@name = 'leaveType']//button"
    dropdown_Reason_ToSelect = "//ul[@class='dropdown-menu ng-star-inserted']//li//a[text()=' Work from home ']"
    dropdown_from_date_xpath = "//gt-leave-date-picker[@name= 'fromDate' ]//span[text()= ' Select date']"
    dropdown_to_date_xpath = "//gt-leave-date-picker[@name= 'toDate' ]//span[text()= ' Select date']"
    editbox_contact_details_id = "contactDetailsField"
    editbox_reason_id = "reasonField"
    button_from_date_xpath = "//gt-leave-date-picker[@name='fromDate']//*[@class='fa fa-calendar']"
    button_to_date_xpath = "//gt-leave-date-picker[@name='toDate']//*[@class='fa fa-calendar']"
    # button_pick_to_date_xpath = "//gt-leave-date-picker[@name='toDate']//div[@class='gt-emp-leave-calendar']//gt-emp-leave-cal-stripe//p[@class='text-4 date' and contains(text(),'" #'21')]"
    button_pick_to_date_xpath = "//gt-leave-date-picker[@name='toDate']//div[@class='gt-emp-leave-calendar']//tr[@class='ng-star-inserted']//p[(@class='text-4 date gt-calendar-today' or @class='text-4 date') and contains(text(),'"#26')]"
    # button_pick_from_date_xpath = "//gt-leave-date-picker[@name='fromDate']//div[@class='gt-emp-leave-calendar']//gt-emp-leave-cal-stripe//p[@class='text-4 date' and contains(text(),'" #'21')]"
    button_pick_from_date_xpath = "//gt-leave-date-picker[@name='fromDate']//div[@class='gt-emp-leave-calendar']//tr[@class='ng-star-inserted']//p[(@class='text-4 date gt-calendar-today' or @class='text-4 date') and contains(text(),'"#26')]"

    button_submit_xpath = "//button[text()=' Submit ']"

    button_Logout = "//i[@class='icon-gt-power text-1 text-regular text-secondary']"
    webelement_logout_success = "//div[contains(text(),'All done! Have a good time')]"

class Page_Home:
    def __init__(self, driver):
        self.browser = driver
        # import selenium
        # self.browser = selenium.webdriver.Chrome()

    def logout(self):
        self.browser.find_element_by_xpath(Loc_Homepage.button_Logout).click()
        return self.browser.find_element_by_xpath(Loc_Homepage.webelement_logout_success).is_displayed()


    def fill_timesheet(self, reason, s_from, to):
        self.browser.find_element_by_xpath(Loc_Homepage.link_Leave_xpath).click()
        self.browser.find_element_by_xpath(Loc_Homepage.link_My_Leave_xpath).click()
        # leave type droptownToSelect
        # leave_type = Select(self.browser.find_element_by_xpath(Loc_Homepage.dropdown_leave_type_xpath))
        # leave_type.select_by_value(ClassTestVariables.Leave_Type)
        self.browser.find_element_by_xpath(Loc_Homepage.dropdownToClick_leave_type_xpath).click()
        self.browser.find_element_by_xpath(Loc_Homepage.dropdown_Reason_ToSelect).click()

        # Add to and from dates

        # from date
        hp = Loc_Homepage()
        # hp.set_dates(s_from, to)
        self.browser.find_element_by_xpath(Loc_Homepage.button_from_date_xpath).click()
        self.browser.find_element_by_xpath(Loc_Homepage.button_pick_from_date_xpath + s_from + "')]").click()


        # to date
        self.browser.find_element_by_xpath(Loc_Homepage.button_to_date_xpath).click()
        # self.browser.find_element_by_xpath(Loc_Homepage.button_pick_to_date_xpath).click()
        # // gt - leave - date - picker[ @ name = 'toDate'] // div[ @
        # class ='gt-emp-leave-calendar'] // gt-emp-leave-cal-stripe // p[@ class ='text-4 date' and contains(text(), '21')]
        self.browser.find_element_by_xpath(Loc_Homepage.button_pick_to_date_xpath + to + "')]").click()

        #

        self.browser.find_element_by_id(Loc_Homepage.editbox_reason_id).send_keys(reason)
        self.browser.find_element_by_id(Loc_Homepage.editbox_contact_details_id).send_keys(reason)
        # self.browser.find_element_by_xpath(Loc_Homepage.button_submit_xpath).click()
        #
        # self.browser.find_element_by_xpath(Loc_Homepage.button_submit_xpath).click()



