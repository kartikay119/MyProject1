import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from COnfest.password_checker import is_valid_password

class TestRegistration:
    def __init__(self, driver):
        self.driver = driver

    def creating_account(self, name, title, last_name, password, day, month, year):
        try:
            # Select gender
            if title == "Mr":
                self.driver.find_element(By.ID, "id_gender1").click()
            elif title == "Mrs":
                self.driver.find_element(By.ID, "id_gender2").click()
            else:
                raise ValueError("Invalid title. Use 'Mr' or 'Mrs'.")

            # Fill in the form
            self.driver.find_element(By.ID, "customer_firstname").send_keys(name)
            self.driver.find_element(By.ID, "customer_lastname").send_keys(last_name)

            # Validate password
            if is_valid_password(password) != "Valid Password":
                raise ValueError("Invalid password. Please follow the password policy.")

            self.driver.find_element(By.ID, "passwd").send_keys(password)

            # Select date of birth
            Select(self.driver.find_element(By.ID, "days")).select_by_value(day)
            Select(self.driver.find_element(By.ID, "months")).select_by_value(month)
            Select(self.driver.find_element(By.ID, "years")).select_by_value(year)

            # Subscribe to the newsletter
            self.driver.find_element(By.ID, "newsletter").click()

        except NoSuchElementException as e:
            print(f"Error: Element not found - {e}")
        except ValueError as e:
            print(f"Input Error: {e}")

    def register_button(self):
        try:
            self.driver.find_element(By.ID, "submitAccount").click()
            print("Registration button clicked successfully.")
        except NoSuchElementException:
            print("Error: Submit button not found.")
