import time

from appium import webdriver
import pytest


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
        driver.find_element_by_xpath('hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
        time.sleep(5)
        driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signInOutButton').click()
        time.sleep(5)
        driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input').send_keys("new_user_1606759264")
        time.sleep(5)
        driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input').send_keys("Test1234")
        time.sleep(5)
        driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/sign_in_button').click()
        time.sleep(5)
        arg_text = driver.find_element_by_id('ar.com.bancar.uala.cryptoapp.stage:id/environmentText').text
        assert arg_text == 'Argentina (STAGE)'





