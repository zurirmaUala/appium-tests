from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageBuyCrypto:
    def __init__(self, driver):
        self.header_amount_balance = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/headerAmountBalance')
        self.estimated_crypto = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText')
        self.local_currency_field = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')
        self.total_text = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/totalText')
        self.confirmation_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')
        self.driver = driver

    def get_header_amount_balance(self):
        header_amount_balance = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.header_amount_balance))
        return header_amount_balance

    def get_total_text(self):
        total_text = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            self.total_text))
        return total_text

    def input_local_currency(self, amount):
        local_currency_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.local_currency_field))
        local_currency_field.send_keys(str(amount))

    def select_buy_crypto(self):
        confirmation_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            self.confirmation_button))
        confirmation_button.click()
