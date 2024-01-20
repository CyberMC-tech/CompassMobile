# webdriver/login.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from webdriver.constants import username_field_id, password_field_id, login_url


class MyWebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # Add any other necessary WebDriver initialization here

    def login(self, username, password):
        try:
            self.driver.get(login_url)

            # Assuming there are fields for username and password
            username_field = self.driver.find_element(by=By.ID, value=username_field_id)
            password_field = self.driver.find_element(by=By.ID, value=password_field_id)

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            # Add logic to check for successful login, etc.
            return True  # or some relevant status/message

        except WebDriverException as e:
            print(f"Error during login: {e}")
            return False  # or some error code/message

    def fetch_data(self):
        # Add logic to fetch specific data after login
        # TODO: add login to get all data, cache it, and close the webdriver.
        pass

    def close(self):
        self.driver.quit()
