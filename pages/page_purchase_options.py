from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PagePurchaseOptions():
    def __init__(self, driver):
        self.btc_button = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup')
        self.driver = driver

    def select_btc_option(self):
        btc_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btc_button))
        btc_button.click()












