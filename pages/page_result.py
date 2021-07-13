from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageResult:
    def __init__(self, driver):
        self.feedback_icon = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_icon')
        self.feedback_title = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_title')
        self.feedback_subtitle = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_subtitle')
        self.back_home_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_primary_action')
        self.driver = driver

    def get_feedback_icon(self):
        feedback_icon = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.feedback_icon))
        return feedback_icon

    def get_feedback_title(self):
        feedback_title = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(
            self.feedback_title))
        return feedback_title.text

    def get_feedback_subtitle(self):
        feedback_subtitle = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.feedback_subtitle))
        return feedback_subtitle

    def press_back_home_button(self):
        back_home_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.back_home_button))
        back_home_button.click()
