from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class FormBasic:
    EXPERIENCE = (By.ID, 'exp')
    JAVA = (By.ID, 'check_java')
    SELENIUM = (By.ID, 'rad_selenium')
    PRIMARY_DROPDOWN = (By.XPATH, '//select[@id="select_tool"]')
    SELECT_LANG = (By.ID, 'select_lang')
    NOTES = (By.ID, 'notes')
    COMMON_SENSE = (By.ID, 'common_sense')
    SPEAKS_GERMAN = (By.ID, 'german')
    FLUENCY = (By.ID, 'fluency')
    UPLOAD_CV = (By.ID, 'upload_cv')
    UPLOAD_FILES = (By.ID, 'upload_files')
    SALARY = (By.ID, 'salary')
    CITY = (By.ID, 'validationCustom03')
    STATE = (By.ID, 'validationCustom04')
    ZIP = (By.ID, 'validationCustom05')
    AGREE_CHECKBOX = (By.ID, 'invalidCheck')
    SUBMIT_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
    ASSERTION_ELEMENTS = (By.XPATH, '//span[@class="form-text text-success"]')
    INPUT_NON_ENGLISH = (By.ID, 'नाव')
    CHECKBOX1_NON_ENGLISH = (By.ID, 'मराठी')
    CHECKBOX2_NON_ENGLISH = (By.ID, 'ગુજરાતી')
    CHECKBOX3_NON_ENGLISH = (By.ID, 'ਪੰਜਾਬੀ')

    def __init__(self, driver):
        self.driver = driver

    def experience(self, text):
        self.driver.find_element(*self.EXPERIENCE).clear()
        self.driver.find_element(*self.EXPERIENCE).send_keys(text + Keys.RETURN)

    def primary_skills(self):
        skills = Select(self.driver.find_element_by_xpath('//select[@id="select_tool"]'))
        skills.select_by_index(2)

    def select_language(self):
        language = Select(self.driver.find_element_by_xpath('//select[@id="select_lang"]'))
        language.select_by_index(2)
        o = language.first_selected_option
        print("Selected option is: " + o.text)

    def check_language_box(self):
        self.driver.find_element(*self.JAVA).click()

    def check_skill_box(self):
        self.driver.find_element(*self.SELENIUM).click()
        assert self.driver.find_element(*self.SELENIUM).is_displayed()

    def note(self, text):
        self.driver.find_element(*self.NOTES).clear()
        self.driver.find_element(*self.NOTES).send_keys(text + Keys.RETURN)

    def check_mandatory_skill_box(self):
        return self.driver.find_element(*self.COMMON_SENSE).get_attribute("placeholder")

    def check_speak_german_option(self):
        option = self.driver.find_element(*self.SPEAKS_GERMAN)
        self.driver.execute_script("arguments[0].click();", option)

    def check_fluency_level(self):
        slider = self.driver.find_element(*self.FLUENCY)
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(150, 0).release().perform()

    def check_current_salary_box(self):
        return self.driver.find_element(*self.SALARY).get_attribute("placeholder")

    def check_city(self, text):
        self.driver.find_element(*self.CITY).clear()
        self.driver.find_element(*self.CITY).send_keys(text + Keys.RETURN)

    def city_presence(self):
        assert self.driver.find_element(*self.CITY).is_displayed()

    def check_state(self, text):
        self.driver.find_element(*self.STATE).clear()
        self.driver.find_element(*self.STATE).send_keys(text + Keys.RETURN)

    def state_presence(self):
        assert self.driver.find_element(*self.STATE).is_displayed()

    def check_zip(self, text):
        self.driver.find_element(*self.ZIP).clear()
        self.driver.find_element(*self.ZIP).send_keys(text + Keys.RETURN)

    def zip_presence(self):
        assert self.driver.find_element(*self.ZIP).is_displayed()

    def check_terms_box(self):
        self.driver.find_element(*self.AGREE_CHECKBOX).click()

    def terms_presence(self):
        assert self.driver.find_element(*self.AGREE_CHECKBOX).is_displayed()

    def check_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def check_input_non_english(self, text):
        self.driver.find_element(*self.INPUT_NON_ENGLISH).clear()
        self.driver.find_element(*self.INPUT_NON_ENGLISH).send_keys(text + Keys.RETURN)

    def input_non_english_presence(self):
        assert self.driver.find_element(*self.INPUT_NON_ENGLISH).is_displayed()

    def check_checkbox1_non_english(self):
        self.driver.find_element(*self.CHECKBOX1_NON_ENGLISH).click()

    def check_checkbox2_non_english(self):
        self.driver.find_element(*self.CHECKBOX2_NON_ENGLISH).click()

    def check_checkbox3_non_english(self):
        self.driver.find_element(*self.CHECKBOX3_NON_ENGLISH).click()

    def verifyMsg(self):
        assert_element = self.driver.find_elements(*self.ASSERTION_ELEMENTS)
        listOfElements = []
        for element in assert_element:
            listOfElements.append(element.text)
        return listOfElements
