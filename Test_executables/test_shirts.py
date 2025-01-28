import time

from Test_cases.shirt import Testshirt
import pytest
from selenium import webdriver
@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.automationpractice.pl/index.php?controller=search&orderby=position&orderway=desc&search_query=T-shirts&submit_search=")
    yield driver
    driver.quit()
def test_shirt(driver):
    t= Testshirt(driver)
    t.shirt_more()
    t.drop_down()
    time.sleep(5)
    t.Add_cart()
