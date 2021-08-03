from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from browser_main import BrowserMainSetUp  # i might use this in the future

browserMain = BrowserMainSetUp
ignored_exceptions = (
    NoSuchElementException, StaleElementReferenceException,)


class Browser:
    def __init__(self):
        self.driver = None
        self.actions = None

        self.PATH = "Driver\chromedriver.exe"

        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException,)

    def run(self, command):  # i'm going to use this later to make the code look cleaner
        if "Google" in command:
            self.google()
        elif "Bing" in command:
            self.bing()
        elif "College" in command:
            self.college()

    def google(self):
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.google.com/")

    def bing(self):
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://www.bing.com/")

    def college(self):
        global buttonNext
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://howdy.tamu.edu/uPortal/normal/render.uP")
        try:
            loginButton = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="loginbtn"]')))
        finally:
            loginButton.click()

        while True:
            text = browserMain.get_audio()
            text = text.lower()
            if "close browser" in text:
                self.driver.close()
                print("[Kanna-Chan]: closing browser")
                browserMain.speak("closing browser")
                break
            if "login" in text: # I cannot deal with the duo two auth passwqord problem: https://gateway.tamu.edu/settings
                try:
                    userLoginInput = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
                    passwordLoginInput = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
                    buttonNext = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fm1"]/button')))
                except Exception as e:
                    print("error")
                    run = False

                run = True
                while run:
                    print("[Kanna-Chan]: Type in your username")
                    browserMain.speak("Type in your username")

                    username = input("Username: ")

                    print("[Kanna-Chan]: Type in your password")
                    browserMain.speak("Type in your password")

                    password = input("Password: ")

                    try:
                        userLoginInput.send_keys(username)
                        passwordLoginInput.send_keys(password)

                        buttonNext.click()
                    except Exception as e:
                        print("error")

                    # login correctly?
                    try:
                        loginError = WebDriverWait(self.driver, 5, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_error"]')))
                        print("[Error-Chan]: Password Or Email is Wrong \n Restarting...")
                        self.driver.refresh()
                    except Exception as e:
                        run = False