from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginBackend:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://compassmobile.dollartree.com/")
        self.username_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "idUNField")))
        self.password_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "idPWField")))
        self.login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))

    def login(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.login_button.click()


if __name__ == "__main__":
    pass
