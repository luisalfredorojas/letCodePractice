from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LetCodePage:
        input_card = (By.XPATH,
                      '/html/body/app-root/app-test-site/section[2]/div/div/div/div[1]/app-menu/div/footer/a')
        input_full_name = (By.ID, 'fullName')
        input_append_a_text_and_tab = (By.ID, 'join')
        input_text_inside_the_box = (By.ID, 'getMe')
        input_clear_text = (By.ID, 'eraseMe')








