from selenium.webdriver.support.select import Select

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from TestData import TestVariables


class Loc_Login():
    # for Login
    editbox_username = "txtUserName"
    editbox_password = "txtPwd"
    button_login = "imgLogin"


class Loc_TimeSheet():
    link_nTrack = "imgbtnNTrack"
    link_project = "FITCHDPC"
    link_timesheet = "Timesheet"
    radiobutton_tasktype = "rboYes"
    editbox_task = "txtTask"
    dropdown_projectcode = "//select[@name='cboProjectCode']"
    # Activity
    dropdown_activity = "//select[@name='cboActivity']"
    EditBox_Comments = "txtComment"
    EditBox_EstimatedEffort = "txtEstEffort"
    EditBox_Effort = "txtEffort"
    Button_Submit = "btnUSubmit"
    Button_Cancel_extra_hours = "//*[@id='btnCancelmsg']"
