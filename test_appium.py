import time
import allure
from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import page_buy_crypto
from pages import page_landing
from pages import page_buy_crypto
from pages import page_result
from pages import page_loading
from pages import page_confirmation_purchase
from pages import page_countries
from pages import page_pre_login
from pages import page_purchase_options
from pages.page_buy_crypto import PageBuyCrypto
from pages.page_confirmation_purchase import PageConfirmationPurchase
from pages.page_countries import PageCountries
from pages.page_landing import PageLanding
from pages.page_loading import PageLoading
from pages.page_login import PageLogin
from pages.page_pre_login import PagePreLogin
from pages.page_purchase_options import PagePurchaseOptions
from pages.page_result import PageResult

desired_caps = {
    "browser": "appium",
    "wait_time": 10,
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "ar.com.bancar.uala.cryptoapp.stage",
    "appActivity": "ar.com.bancar.uala.cryptoapp.ui.SelectEnvironmentActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


class Testappium():
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        """Test que valida un logueo exitoso a la app"""
        page_country = PageCountries(driver)
        pre_login = PagePreLogin(driver)
        login = PageLogin(driver)
        page_country.select_arg_button()
        pre_login.select_iniciar_sesion_button()
        login.input_name()
        login.input_password()
        login.press_sign_in_button()
        time.sleep(20)
        text = pre_login.get_environment_text()
        assert 'Argentina (STAGE)' == text

        # wait = WebDriverWait(driver, 20)
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')))
        # # driver.find_element_by_xpath('hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signInOutButton')))
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input')))
        # currently_waiting_for.send_keys("new_user_1606759264")
        # # driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input').send_keys("new_user_1606759264")
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input')))
        # currently_waiting_for.send_keys("Test1234")
        # # driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input').send_keys("Test1234")
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/sign_in_button')))
        # currently_waiting_for.click()
        # arg_text = wait.until(EC.text_to_be_present_in_element((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/environmentText'),'Argentina (STAGE)'))
        # # arg_text.text
        # assert arg_text == True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase(self):
        """Test que valida una compra de btc exitosa"""
        crypto = PagePreLogin(driver)
        landing = PageLanding(driver)
        btc = PagePurchaseOptions(driver)
        buy_crypto = PageBuyCrypto(driver)
        confirmation = PageConfirmationPurchase(driver)
        result = PageResult(driver)
        loading = PageLoading(driver)
        crypto.select_ir_a_inv_crypto_button()
        landing.select_purchase_button()
        btc.select_btc_option()
        buy_crypto.input_local_currency('100,00')
        buy_crypto.select_buy_crypto()
        confirmation.confirm_purchase()
        time.sleep(30)
        assert 'Danos un minuto' == loading.get_feedback_title()
        time.sleep(45)
        assert '¡Se generó la compra!' == result.get_feedback_title()






        # wait = WebDriverWait(driver, 90)
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/go_to_exchange_button')))
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView')))
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup')))
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')))
        # currently_waiting_for.send_keys('100,00')
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')))
        # currently_waiting_for.click()
        # currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')))
        # currently_waiting_for.click()
        # successful_text = wait.until(EC.text_to_be_present_in_element((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/feedback_title'),'¡Se generó la compra!'))
        # assert successful_text == True
    @allure.severity(allure.severity_level.BLOCKER)
    def test_another(self):
        """Another case..."""
        assert False






