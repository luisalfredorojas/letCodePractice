
from selenium import webdriver

import data
import metodos


class TestLetCode:
    driver = None


    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_click_app_menu(self):
        self.driver.get(data.URL)
        methods = metodos.LetCodeMethods(self.driver)
        methods.to_be_clickable_input_menu()
        methods.click_input_menu()

    def test_inputs_full_name(self):
        methods = metodos.LetCodeMethods(self.driver)
        self.test_click_app_menu()
        methods.to_be_clickable_input_full_name()
        methods.send_keys_input_full_name()

    def test_inputs_append_text(self):
        methods = metodos.LetCodeMethods(self.driver)
        self.test_inputs_full_name()
        current_text = methods.get_value_append_text_name()
        methods.send_keys_tab_input_full_name()
        methods.send_keys_tab_append_text_name()
        new_text = methods.get_text_append_text_name()
        assert new_text != current_text
        whats_inside_the_box = methods.get_text_in_inside_the_input()
        assert whats_inside_the_box != " "
        methods.erase_text_inside_box_erase_me()
        erase_me_new_value = methods.get_value_text_inside_box_erase_me()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

