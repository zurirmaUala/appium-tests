from appium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
    def test_model(self):
        assert True

    def test_login(self):
        wait = WebDriverWait(driver, 20)
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')))
        # driver.find_element_by_xpath('hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signInOutButton')))
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input')))
        currently_waiting_for.send_keys("new_user_1606759264")
        # driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input').send_keys("new_user_1606759264")
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input')))
        currently_waiting_for.send_keys("Test1234")
        # driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input').send_keys("Test1234")
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/sign_in_button')))
        currently_waiting_for.click()
        arg_text = wait.until(EC.text_to_be_present_in_element((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/environmentText'),'Argentina (STAGE)'))
        # arg_text.text
        assert arg_text == True

    def test_purchase(self):
        wait = WebDriverWait(driver, 90)
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/go_to_exchange_button')))
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView')))
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup')))
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText')))
        currently_waiting_for.send_keys('100,00')
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')))
        currently_waiting_for.click()
        currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/confirmationButton')))
        currently_waiting_for.click()
        successful_text = wait.until(EC.text_to_be_present_in_element((By.ID,'ar.com.bancar.uala.cryptoapp.stage:id/feedback_title'),'¡Se generó la compra!'))
        assert successful_text == True







