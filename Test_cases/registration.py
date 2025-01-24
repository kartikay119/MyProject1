import time

from selenium.webdriver.common.by import By


class Testregistration1:
    def __init__(self,driver):
        self.driver=driver
        self.email='//*[@id="email_create"]'
        self.create_account_button='/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]/button/span'

    def registration1(self,email):
        input1 = self.driver.find_element(By.XPATH,self.email)
        input1.send_keys(email)
        self.driver.find_element(By.XPATH,self.create_account_button).click()
        time.sleep(3)
        a = self.driver.find_element(By.CLASS_NAME,"page-heading").text
        yield a








