from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    
    def __init__(self, driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))):
        self.driver = driver 
        self.base_url = 'https://opensource-demo.orangehrmlive.com/'

    def find_element(self, locator):
        e = self.driver.find_element(locator[0], locator[1])
        return e

    def find_elements(self, locator):
        e = self.driver.find_elements(locator[0], locator[1])
        return e

    def go_to_site(self):
        r = self.driver.get(self.base_url)
        return r