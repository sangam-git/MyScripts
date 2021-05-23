import selenium
from selenium import webdriver


class ClassTestVariables:
    CHROME_PATH = "../Browsers/chromedriver.exe"
    URL = "https://entity.nousinfo.com/commonlogin/Login.aspx"
    Username = "NST21501"
    Password = "nous;" + Username
    Timeout = "20"
    Activity = "Scripting"
    Efforts = "8"
    EstimatedEfforts = Efforts
    Project = "FITCHDPC"
    Task = "Fitch Task"
    Comments = "Fitch Scripting"
    browser = selenium.webdriver
    TaskType = "Daily"
