from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
class Testshirt:
    def __init__(self,driver):
        self.driver=driver
    def shirt_more(self):
        self.driver.find_element(By.XPATH,'//*[@id="best-sellers_block_right"]/div/ul/li[4]/a').click()
    def drop_down(self):
        a = Select(self.driver.find_element(By.XPATH,'//*[@id="group_1"]'))
        a.select_by_visible_text("M")
    def Add_cart(self):
        add = self.driver.find_element(By.XPATH,'//*[@id="add_to_cart"]/button')
        add.click()




