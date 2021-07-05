from appium import webdriver
import pytest


desired_caps = {
    "browser": "appium",
    "wait_time": 10,
    "deviceName": "Pixel2.5.11",
    "platformName": "Android",
    "appPackage": "ar.com.bancar.uala.cryptoapp.stage",
    "appActivity": "ar.com.bancar.uala.cryptoapp.ui.SelectEnvironmentActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
class Testappium():
    def test_model(self):
        assert True

    def test_login(self):
        driver.find_element_by_xpath('hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]').click()






