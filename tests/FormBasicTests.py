import unittest
from utils.SetupPage import SetupPage
from pageObjects.FormBasic import FormBasic


class FormBasicTests(unittest.TestCase):

    def setUp(self):
        self.driver = SetupPage().getBrowser("https://dineshvelhal.github.io/testautomation-playground/forms.html")
        self.formBasicPage = FormBasic(self.driver)

    def testForm(self):
        exp = "5"
        primary_skills = "cyp"
        language = "javascript"
        language_box = "JAVA"
        skill_box = "SELENIUM"
        common_sense = "Common Sense"
        german_option = "true"
        fluency_level = "5"
        notes = "something tot note"
        current_salary = "You should not provide this"
        city = "oradea"
        state = "california"
        zip_code = "770208"
        input_non_english = "non english"
        checkbox1_non_english = "मराठी"
        checkbox2_non_english = "मराठी ગુજરાતી"
        checkbox3_non_english = "मराठी ગુજરાતી ਪੰਜਾਬੀ"
        self.formBasicPage.experience(exp)
        assert self.formBasicPage.verifyMsg().__contains__(exp)
        self.formBasicPage.primary_skills()
        assert self.formBasicPage.verifyMsg().__contains__(primary_skills)
        self.formBasicPage.select_language()
        assert self.formBasicPage.verifyMsg().__contains__(language)
        self.formBasicPage.check_language_box()
        assert self.formBasicPage.verifyMsg().__contains__(language_box)
        self.formBasicPage.check_skill_box()
        assert self.formBasicPage.verifyMsg().__contains__(skill_box)
        self.formBasicPage.check_mandatory_skill_box()
        assert self.formBasicPage.check_mandatory_skill_box().__contains__(common_sense)
        self.formBasicPage.check_speak_german_option()
        assert self.formBasicPage.verifyMsg().__contains__(german_option)
        self.formBasicPage.check_fluency_level()
        assert self.formBasicPage.verifyMsg().__contains__(fluency_level)
        self.formBasicPage.note(notes)
        assert self.formBasicPage.verifyMsg().__contains__(notes)
        self.formBasicPage.check_current_salary_box()
        assert self.formBasicPage.check_current_salary_box().__contains__(current_salary)
        self.formBasicPage.check_city(city)
        self.formBasicPage.city_presence()
        self.formBasicPage.check_state(state)
        self.formBasicPage.state_presence()
        self.formBasicPage.check_zip(zip_code)
        self.formBasicPage.zip_presence()
        self.formBasicPage.check_terms_box()
        self.formBasicPage.terms_presence()
        self.formBasicPage.check_input_non_english(input_non_english)
        assert self.formBasicPage.verifyMsg().__contains__(input_non_english)
        self.formBasicPage.check_checkbox1_non_english()
        assert self.formBasicPage.verifyMsg().__contains__(checkbox1_non_english)
        self.formBasicPage.check_checkbox2_non_english()
        assert self.formBasicPage.verifyMsg().__contains__(checkbox2_non_english)
        self.formBasicPage.check_checkbox3_non_english()
        assert self.formBasicPage.verifyMsg().__contains__(checkbox3_non_english)
        self.formBasicPage.check_submit_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
