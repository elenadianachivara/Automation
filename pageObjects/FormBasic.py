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

    def __init__(self, driver):
        self.driver = driver

    def experience(self, text):
        self.driver.find_element(*self.EXPERIENCE).clear()
        self.driver.find_element(*self.EXPERIENCE).send_keys(text + Keys.RETURN)
        assert self.driver.find_element_by_xpath(
            '//span[@class="form-text text-success" and text()="5"]').is_displayed()

    def primary_skills(self):
        s = Select(self.driver.find_element_by_xpath('//select[@id="select_tool"]'))
        s.select_by_index(2)
        o = s.first_selected_option
        print("Selected option is: " + o.text)

    def select_language(self):
        s = Select(self.driver.find_element_by_xpath('//select[@id="select_lang"]'))
        s.select_by_index(2)
        o = s.first_selected_option
        print("Selected option is: " + o.text)

    def check_language_box(self):
        self.driver.find_element(*self.JAVA).click()

    def check_skill_box(self):
        self.driver.find_element(*self.SELENIUM).click()
        assert self.driver.find_element(*self.SELENIUM).is_displayed()

    def check_mandatory_skill_box(self):
        a = self.driver.find_element(*self.COMMON_SENSE).get_attribute("placeholder")
        print("Selected option is: " + a)

    def check_speak_german_option(self):
        a = self.driver.find_element(*self.SPEAKS_GERMAN)
        self.driver.execute_script("arguments[0].click();", a)

    def check_flunecy_level(self):
        slider = self.driver.find_element(*self.FLUENCY)
        move = ActionChains(self.driver)
        move.click_and_hold(slider).move_by_offset(150, 0).release().perform()

        # move.click_and_hold(slider).move_by_offset(random.randint(0, 5), 0).release().perform()

    def verifyMsg(self):
        assert_element = self.driver.find_elements(*self.ASSERTION_ELEMENTS)
        listOfElements = []
        for element in assert_element:
            listOfElements.append(element.text)
        return listOfElements
