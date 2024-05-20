from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


class LetCodeMethods:
    import locators
    locators_page = locators.LetCodePage

    def __init__(self, driver):
        self.driver = driver

    def to_be_clickable_input_menu(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.locators_page.input_card))

    def click_input_menu(self):
        self.driver.find_element(*self.locators_page.input_card).click()

    def to_be_clickable_input_full_name(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.locators_page.input_full_name))

    def send_keys_input_full_name(self):
        self.driver.find_element(*self.locators_page.input_full_name).send_keys('Luis Alfredo Rojas Munoz')

    def send_keys_tab_input_full_name(self):
        self.driver.find_element(*self.locators_page.input_full_name).send_keys(Keys.TAB)

    def get_value_append_text_name(self):
        return self.driver.find_element(*self.locators_page.input_append_a_text_and_tab).get_attribute("value")

    def get_text_append_text_name(self):
        return self.driver.find_element(*self.locators_page.input_append_a_text_and_tab).text

    def send_keys_input_append_text_name(self):
        self.driver.find_element(*self.locators_page.input_append_a_text_and_tab).send_keys('This is a text append')

    def send_keys_tab_append_text_name(self):
        self.driver.find_element(*self.locators_page.input_append_a_text_and_tab).send_keys(Keys.TAB)

    def get_text_in_inside_the_input(self):
        return self.driver.find_element(*self.locators_page.input_text_inside_the_box).get_attribute("value")

    def send_tab_in_inside_the_input(self):
        return self.driver.find_element(*self.locators_page.input_text_inside_the_box).send_keys(Keys.TAB)

    def erase_text_inside_box_erase_me(self):
        self.driver.find_element(*self.locators_page.input_clear_text).exe("value", " ")

    def get_value_text_inside_box_erase_me(self):
        return self.driver.find_element(*self.locators_page.input_clear_text).get_attribute("value")





