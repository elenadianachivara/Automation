from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InputFormPage:
    INPUT = (By.NAME, 'name')

    def __init__(self, driver):
        self.driver = driver

    def inputForm(self, text):
        self.driver.find_element(*self.INPUT).clear
        self.driver.find_element(*self.INPUT).send_keys(text + Keys.RETURN)

    def inputForm_presence(self):
        assert self.driver.find_element(*self.INPUT).is_displayed()
