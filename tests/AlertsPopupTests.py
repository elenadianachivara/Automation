import unittest
from utils.SetupPage import SetupPage
from pageObjects.AlertsPopupPage import AlertsPopupPage


class AlertsPopupTests(unittest.TestCase):

    def setUp(self):
        self.driver = SetupPage().getBrowser("https://www.way2automation.com/way2auto_jquery/alert.php#load_box")
        self.alerts = AlertsPopupPage(self.driver)

    def testAlert(self):
        self.alerts.clickButton()
        assert self.alerts.getAlertMessage().__contains__("I am an alert box!")
        self.alerts.closeAlertPopup()

    def tearDown(self):
        self.driver.quit()
