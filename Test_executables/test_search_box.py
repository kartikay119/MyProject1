# import time
# from selenium import webdriver
# from Test_cases.search_box import search_box
# from selenium.webdriver.common.by import By
# import  pytest
#
# class search_text:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def search(self, text):
#         text_input = self.driver.find_element(By.XPATH, '//*[@id="search_query_top"]')
#         text_input.send_keys(text)
#         s_button = self.driver.find_element(By.XPATH,'//*[@id="searchbox"]/button')
#         s_button.click()
#         time.sleep(5)
#         sort = self.driver.find_element(By.XPATH, '//*[@id="selectProductSort"]/option[6]')
#         sort.click()
#         time.sleep(5)
#
#
# @pytest.fixture(scope="class")
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
#     yield driver
#     driver.quit()
#
# @pytest.mark.parametrize("text",["T-Shirts"])
# def search_button(driver,text):
#     r = search_box(driver)
#     time.sleep(5)
#     a=r.input(text)
#     time.sleep(5)
#

