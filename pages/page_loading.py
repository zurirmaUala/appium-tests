from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageLoading:
    def __init__(self, driver):
        self.feedback_title = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_title')
        self.feedback_subtitle = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_subtitle')
        self.feedback_primary_action_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/feedback_primary_action')
        self.driver = driver

    def get_feedback_title(self):
        feedback_title = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.feedback_title))
        return feedback_title

    def get_feedback_subtitle(self):
        feedback_subtitle = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.feedback_subtitle))
        return feedback_subtitle

    def press_feedback_primary_action_button(self):
        feedback_primary_action_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.feedback_primary_action_button))
        feedback_primary_action_button.click()

