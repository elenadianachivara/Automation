from selenium.webdriver.common.by import By


class AlertsPopupPage:
    BUTTON = (By.XPATH, '//button[@onclick="myFunction()"]')
    IFRAME = (By.XPATH, "(//iframe[@class='demo-frame'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def clickButton(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME))
        self.driver.find_element(*self.BUTTON).click()

    def getAlertMessage(self):
        return self.driver.switch_to.alert.text

    def closeAlertPopup(self):
        self.driver.switch_to.alert.accept()

