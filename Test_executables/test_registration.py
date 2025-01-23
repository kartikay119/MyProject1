import time

from selenium import webdriver
import pytest
from Test_cases.registration import Testregistration
@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()
@pytest.mark.parametrize("email",["bkartikay82@gmail.com"])
def test_registration1(driver,email):
    r = Testregistration(driver)
    time.sleep(5)
    a=r.registration1(email)
    time.sleep(5)
    # assert a == "CREATE AN ACCOUNT", "Not working"
