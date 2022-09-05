from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SetupPage:

    def __init__(self):
        self.driver = None

    def getBrowser(self, url):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        return self.driver
