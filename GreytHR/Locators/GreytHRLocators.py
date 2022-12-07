from selenium.webdriver.support.select import Select

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains


class Loc_Login:
    # for Login
    editbox_username_name = "username"
    editbox_password_name = "password"
    button_login_xpath = "//button[@type='submit']"


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
    button_submit_xpath = "//button[text()=' Submit ']"

    # button_pick_to_date_xpath = "//gt-leave-date-picker[@name='toDate']//div[@class='gt-emp-leave-calendar']//gt-emp-leave-cal-stripe//p[@class='text-4 date' and contains(text(),'" #'21')]"
    button_pick_to_date_xpath = "//gt-leave-date-picker[@name='toDate']//div[@class='gt-emp-leave-calendar']//tr[@class='ng-star-inserted']//p[(@class='text-4 date gt-calendar-today' or @class='text-4 date') and contains(text(),'"#26')]"
    # button_pick_from_date_xpath = "//gt-leave-date-picker[@name='fromDate']//div[@class='gt-emp-leave-calendar']//gt-emp-leave-cal-stripe//p[@class='text-4 date' and contains(text(),'" #'21')]"
    button_pick_from_date_xpath = "//gt-leave-date-picker[@name='fromDate']//div[@class='gt-emp-leave-calendar']//tr[@class='ng-star-inserted']//p[(@class='text-4 date gt-calendar-today' or @class='text-4 date') and contains(text(),'"#26')]"