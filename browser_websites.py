from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    def __init__(self):
        self.driver = None
        self.actions = None
        self.PATH = "Driver\chromedriver.exe"
        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException,)

    def google(self):
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.google.com/")
