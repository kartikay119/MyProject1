# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
# class search_box:
#     def __init__(self,driver):
#         self.driver=driver
#         self.input_text = '//*[@id="search_query_top"]'
#         self.s_button = '//*[@id="searchbox"]/button'
#         self.sort = '//*[@id="selectProductSort"]/option[6]]'
#
#
#     def input(self,text):
#         self.driver.find_element(By.ID,self.input_text).send_keys(text)
#         self.driver.find_element(By.NAME,self.s_button).click()
#         self.driver.find_element(By.XPATH,self.sort).click()
#         self.driver.find_element(By.LINK_TEXT,'Printed Summer Dress').click()
#         drpdwn = Select(self.driver.find_element(By.XPATH,'//*[@id="group_1"]/option[2]'))
#         drpdwn.select_by_value('2')
#
#     def Add_button(self):
#         self.driver.find_element(By.NAME,"Submit").click()
