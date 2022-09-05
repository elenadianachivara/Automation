import unittest
from utils.SetupPage import SetupPage
from pageObjects.FormBasic import FormBasic


class FormBasicTests(unittest.TestCase):

    def setUp(self):
        self.driver = SetupPage().getBrowser("https://dineshvelhal.github.io/testautomation-playground/forms.html")
        self.formBasicPage = FormBasic(self.driver)

    def testExample(self):
        exp = "5"
        self.formBasicPage.experience(exp)
        assert self.formBasicPage.verifyMsg().__contains__(exp)
        self.formBasicPage.primary_skills()
        self.formBasicPage.select_language()
        self.formBasicPage.check_language_box()
        self.formBasicPage.check_skill_box()
        self.formBasicPage.check_mandatory_skill_box()
        self.formBasicPage.check_speak_german_option()
        self.formBasicPage.check_flunecy_level()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
