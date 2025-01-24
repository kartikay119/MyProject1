    # import time
    #
    # from selenium import webdriver
    # import pytest
    # from Test_cases.registration import Testregistration
    # from Test_cases.create_account import Testregistration1
    #
    # @pytest.fixture(scope="class")
    # def driver():
    #     driver=webdriver.Chrome()
    #     driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    #     yield driver
    #     driver.quit()
    # @pytest.mark.parametrize("name,title, last_name,email, password, day, month , years",[("Kartikay","Mr","Kar","kartikay119@gmail.com","12345",'1',"1","1999")])
    # def test_create(name,title, last_name,email, password, day, month , years,driver):
    #     r = Testregistration(driver)
    #     time.sleep(8)
    #     c= Testregistration1(driver)
    #     time.sleep(8)
    #     r.registration1(email)
    #     time.sleep(8)
    #     c.creating_account(name,title, last_name, password, day, month , years)
    #     time.sleep(8)
    #
    #     c.register_button()
    #     time.sleep(8)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# Class for the registration process
class Testregistration:
    def __init__(self, driver):
        self.driver = driver

    def registration1(self, email):
        email_input = self.driver.find_element(By.ID, "email_create")
        email_input.clear()
        email_input.send_keys(email)
        create_account_button = self.driver.find_element(By.ID, "SubmitCreate")
        create_account_button.click()

# Class for creating an account
class Testregistration1:
    def __init__(self, driver):
        self.driver = driver

    def creating_account(self, name, title, last_name, password, day, month, years):
        if title == "Mr":
            self.driver.find_element(By.ID, "id_gender1").click()
        elif title == "Mrs":
            self.driver.find_element(By.ID, "id_gender2").click()

        self.driver.find_element(By.ID, "customer_firstname").send_keys(name)
        self.driver.find_element(By.ID, "customer_lastname").send_keys(last_name)
        self.driver.find_element(By.ID, "passwd").send_keys(password)
        self.driver.find_element(By.ID, "days").send_keys(day)
        self.driver.find_element(By.ID, "months").send_keys(month)
        self.driver.find_element(By.ID, "years").send_keys(years)

    def register_button(self):
        register_button = self.driver.find_element(By.ID, "submitAccount")
        register_button.click()

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, title, last_name, email, password, day, month, years", [
    ("Kartikay", "Mr", "Kar", "kartikay119@gmail.com", "12345", '1', 'January', '1999')])
def test_create(name, title, last_name, email, password, day, month, years, driver):
    r = Testregistration(driver)
    time.sleep(3)  # Allow page to load
    c = Testregistration1(driver)
    time.sleep(3)  # Allow page to load

    r.registration1(email)
    time.sleep(3)
    c.creating_account(name, title, last_name, password, day, month, years)
    time.sleep(3)
    c.register_button()
    time.sleep(3)
