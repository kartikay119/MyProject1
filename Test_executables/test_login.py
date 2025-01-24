# import time
#
# from selenium import webdriver
# import pytest
# from Test_cases.registration import Testregistration
# from Test_cases.create_account import Testregistration1
# from Test_cases.login_ import TestLogin
#
# @pytest.fixture(scope="class")
# def driver():
#     driver=webdriver.Chrome()
#     # grid_url = "http://127.0.0.1:4444/wd/hub"
#     driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
#     yield driver
#     driver.quit()
# @pytest.mark.parametrize("name,title, last_name,email, password, day, month , years",[("Kartikay","Mr","Bhardwaj","kartikay01@gmail.com","12345",'1',"January","1999")])
# def test_create(name,title, last_name,email, password, day, month , years,driver):
#     r = Testregistration(driver)
#     time.sleep(5)
#     c= Testregistration1(driver)
#     time.sleep(5)
#     r.registration1(email)
#     time.sleep(8)
#     c.creating_account(name,title, last_name, password, day, month , years)
#     time.sleep(5)
#
#     c.register_button()
#     time.sleep(8)
#
#
# @pytest.mark.parametrize("email, password",[("kartikay119@gmail.com","12345")])
# def test_login_functionality(email,password,driver):
#     l = TestLogin(driver)
#     time.sleep(5)
#     l.login_in(email,password)
#     time.sleep(5)
#     l.login_button()
#     time.sleep(4)


import time
from selenium import webdriver
from Test_cases.registration import Testregistration1
from selenium.webdriver.common.by import By
import pytest

# Define Testregistration class
class Testregistration:
    def __init__(self, driver):
        self.driver = driver

    def registration1(self, email):
        email_input = self.driver.find_element(By.ID, "email_create")
        email_input.clear()
        email_input.send_keys(email)
        create_account_button = self.driver.find_element(By.ID, "SubmitCreate")
        create_account_button.click()

# Define Testregistration1 class
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
        self.driver.find_element(By.ID, "submitAccount").click()

# Define TestLogin class
class TestLogin:
    def __init__(self, driver):
        self.driver = driver

    def login_in(self, email, password):
        email_input = self.driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, "passwd")
        password_input.clear()
        password_input.send_keys(password)

    def login_button(self):
        self.driver.find_element(By.ID, "SubmitLogin").click()

# Pytest fixtures and test cases
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, title, last_name, email, password, day, month, years", [
    ("Kartikay", "Mr", "Bhardwaj", "kartikay01@gmail.com", "12345", '1', "January", "1999")
])
def test_create(name, title, last_name, email, password, day, month, years, driver):
    r = Testregistration(driver)
    time.sleep(5)
    c = Testregistration1(driver)
    time.sleep(5)
    r.registration1(email)
    time.sleep(8)
    c.creating_account(name, title, last_name, password, day, month, years)
    time.sleep(5)
    c.register_button()
    time.sleep(8)

@pytest.mark.parametrize("email, password", [
    ("kartikay119@gmail.com", "12345")
])
def test_login_functionality(email, password, driver):
    l = TestLogin(driver)
    time.sleep(5)
    l.login_in(email, password)
    time.sleep(5)
    l.login_button()
    time.sleep(4)

