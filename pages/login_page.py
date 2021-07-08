from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self,driver):
        self.name_field = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/signin_username_input')
        self.password_field = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/signin_password_input')
        self.sign_in_button = (By.ID, 'ar.com.bancar.uala.cryptoapp.stage:id/sign_in_button')

    def input_name(self):
        name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.name_field))
        name.send_keys('new_user_1606759264')

    def input_password(self):
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_field))
        password.send_keys('Test1234')

    def press_sign_in_button(self):
        sign_in = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sign_in_button))
        sign_in.click()









