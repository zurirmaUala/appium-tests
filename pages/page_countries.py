from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageCountries:
    def __init__(self, driver):
        self.arg_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]')
        self.mex_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]')
        self.col_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]')
        self.driver = driver

    def select_arg_button(self):
        argentina_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.arg_button))
        argentina_button.click()

    def select_mex_button(self):
        mexico_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.mex_button))
        mexico_button.click()

    def select_col_button(self):
        colombia_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.col_button))
        colombia_button.click()
