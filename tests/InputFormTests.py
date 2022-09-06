import unittest
from pageObjects.InputForm import InputFormPage
from utils.SetupPage import SetupPage


class InputFormTests(unittest.TestCase):

    def setUp(self):
        self.driver = SetupPage().getBrowser("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
        self.input = InputFormPage(self.driver)

    def testInput(self):
        self.input.inputForm("Diana")
        self.input.inputForm_presence()

    def tearDown(self):
        self.driver.quit()
