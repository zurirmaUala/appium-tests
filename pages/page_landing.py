from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageLanding:
    def __init__(self, driver):
        self.title_page = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/titleBalance')
        self.consolidated_amount = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/amountBalance')
        self.purchase_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView')
        self.sale_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.TextView')
        self.crypto_name = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/crypto_type_tv')
        self.crypto_amount = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/crypto_balance_tv')
        self.local_amount = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/local_amount_balance_tv')
        self.driver = driver

    def compare_title_page(self):
        title = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.title_page), 'Saldo en pesos unificado')

    def check_consolidated_amount(self):
        consolidated_amount = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.consolidated_amount))
        local_amount = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.local_amount))
        assert consolidated_amount == local_amount

    def select_purchase_button(self):
        purchase_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.purchase_button))
        purchase_button.click()

    def select_sale_button(self):
        sale_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sale_button))
        sale_button.click()