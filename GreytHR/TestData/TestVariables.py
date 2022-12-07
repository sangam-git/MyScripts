import selenium
from selenium import webdriver
# having Locators only to set dates.
# from Locators.GreytHRLocators import Loc_Homepage


class ClassTestVariables:
    CHROME_PATH = "../Browsers/chromedriver.exe"
    URL = "https://nousinfosolutions.greythr.com/v3/portal"
    Username = "NST21501"
    Password = "EshMar@2021"
    Timeout = "50"
    Reason = "WFH"
    contact = Reason
    Leave_Type = "Work from home"
    # Leave_Type =  GetData("LeaveTYpe") "Work from home"
