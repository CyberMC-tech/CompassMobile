from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginBackend():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get("https://compassmobile.dollartree.com/")
        self.username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "idUNField")))
        self.password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "idPWField")))
        self.login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))

    def login(self, username, password):
        self.username.clear()
        self.username.send_keys(username)
        self.password.clear()
        self.password.send_keys(password)
        self.login_button.click()


if __name__ == "__main__":
    login = LoginBackend()
    login.options.headless = True
    login.options.enable_mobile()
    login.login()
