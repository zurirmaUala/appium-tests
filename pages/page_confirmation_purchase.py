from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageConfirmationPurchase:
    def __init__(self,driver):
        self.confirm_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')
        self.estimated_local = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/totalAmountText')
        self.estimated_crypto = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/estimatedCryptoText')
        self.warning_advertise = (By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/quote_advertise')
        self.driver = driver

    def confirm_purchase(self):
        purchase_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_button))
        purchase_button.click()

    def get_warning_advertise(self):
        warning = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.warning_advertise), 'Esta cotización es válida por 30 segundos')
        return warning


