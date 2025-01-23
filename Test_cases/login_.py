from selenium.webdriver.common.by import By
import time
class TestLogin:
    def __init__(self,driver):
        self.driver=driver
    def login_in(self,email,password):
        self.driver.find_element(By.ID,"email").send_keys(email)
        self.driver.find_element(By.ID, "passwd").send_keys(password)
        time.sleep(3)
    def login_button(self):
        self.driver.find_element(By.ID,"SubmitLogin").click()