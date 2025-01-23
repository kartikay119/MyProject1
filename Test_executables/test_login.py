import time

import time

from selenium import webdriver
import pytest
from Test_cases.registration import Testregistration
from Test_cases.create_account import Testregistration1
from Test_cases.login_ import TestLogin

@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Chrome()
    grid_url = "http://127.0.0.1:4444/wd/hub"
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()
@pytest.mark.parametrize("name,title, last_name,email, password, day, month , years",[("Name","Mr","Kartikay","kartikay119@gmail.com","12345",'1',"1","1999")])
def test_create(name,title, last_name,email, password, day, month , years,driver):
    r = Testregistration(driver)
    time.sleep(5)
    c= Testregistration1(driver)
    time.sleep(5)
    r.registration1(email)
    time.sleep(8)
    c.creating_account(name,title, last_name, password, day, month , years)
    time.sleep(5)

    c.register_button()
    time.sleep(8)


@pytest.mark.parametrize("email, password",[("kartikay119@gmail.com","12345")])
def test_login_functionality(email,password,driver):
    l = TestLogin(driver)
    time.sleep(5)
    l.login_in(email,password)
    time.sleep(5)
    l.login_button()
    time.sleep(4)
