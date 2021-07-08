from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PagePreLogin:
    def __init__(self, driver):
        self.sing_in_out_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/signInOutButton')
        self.go_to_exchange_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/go_to_exchange_button')
        self.do_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/doButton')
        self.environment_text = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/environmentText')
        self.driver = driver

    def select_iniciar_sesion_button(self):
        sign_in_out_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.sing_in_out_button))
        sign_in_out_button.click()

    def select_ir_a_inv_crypto_button(self):
        go_to_exchange_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.go_to_exchange_button))
        go_to_exchange_button.click()

    def select_empezar_button(self):
        do_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.do_button))
        do_button.click()

    def get_environment_text(self):
        environment_text = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.environment_text))
        return environment_text
