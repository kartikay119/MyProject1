# import time
#
# from selenium import webdriver
# import pytest
# from Test_cases.registration import Testregistration
# @pytest.fixture(scope="class")
# def driver():
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
#     yield driver
#     driver.quit()
# @pytest.mark.parametrize("email",["bkartikay82@gmail.com"])
# def test_registration1(driver,email):
#     r = Testregistration(driver)
#     time.sleep(5)
#     a=r.registration1(email)
#     time.sleep(5)
#     # assert a == "CREATE AN ACCOUNT", "Not working"
#
#

import time
from selenium import webdriver
from Test_cases.registration import Testregistration1
from selenium.webdriver.common.by import By
import pytest

# Define Testregistration class
class Testregistration1:
    def __init__(self, driver):
        self.driver = driver

    def registration1(self, email):
        email_input = self.driver.find_element(By.ID, "email_create")
        email_input.clear()
        email_input.send_keys(email)
        create_account_button = self.driver.find_element(By.ID, "SubmitCreate")
        create_account_button.click()
        time.sleep(5)
        # Return the header text to verify if navigation was successful
        header = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        return header

# Pytest fixtures and test cases
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()

@pytest.mark.parametrize("email", ["bkartikay82@gmail.com"])
def test_registration1(driver, email):
    r = Testregistration1(driver)
    time.sleep(5)
    a = r.registration1(email)
    time.sleep(5)
    # assert a == "CREATE AN ACCOUNT", "Not working"
