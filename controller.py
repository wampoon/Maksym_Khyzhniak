from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Task:
    username_input_id = "txtUsername"
    password_input_id = "txtPassword"
    link = 'https://opensource-demo.orangehrmlive.com/'


    def __init__(self):
        serv = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=serv)
        self.driver.get(self.link)

    def set_username(self,username):
        self.username_input = self.driver.find_element(By.ID, self.username_input_id)
        self.username_input.clear()
        self.username_input.send_keys(username)

    def set_password(self, pwd):
        self.password_input = self.driver.find_element(By.ID, self.password_input_id)
        self.password_input.clear()
        self.password_input.send_keys(pwd)

    def btn_click(self, btn):
        self.driver.find_element(By.XPATH, btn).click()

    def goto_paygrades(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a').click()

    def set_text(self, path, text):
        self.driver.find_element(By.XPATH, path).send_keys(text)

    def check_if_displayed(self, path, desired_text):
        res_bad = 'not found'
        res_good = 'found'
        if (desired_text in self.driver.find_elements(By.XPATH, path)[0].text):
            return res_good
        else: return res_bad

    def finish(self):
        self.driver.close()
        self.driver.quit()

        

# init driver 
s = Task()

# login
s.set_username('Admin')
s.set_password('admin123')
s.btn_click('//*[@id="btnLogin"]')

# going to paygrades
s.goto_paygrades()

# adding random name
s.btn_click('/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]')
s.set_text('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/input[1]', uuid.uuid4().hex[:10])
s.btn_click('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]')

# adding currencies
s.btn_click('/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input')
s.set_text('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/input', 'USD - United States Dollar')
s.set_text('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input', '1')
s.set_text('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input', '5')
s.btn_click('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/p/input[1]')

# checking the presence of added data
print(s.check_if_displayed('/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr', 'United States Dollar'))

# removing added data
s.btn_click('/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr/td[1]/input')
s.btn_click('/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input[2]')

# checking if data was removed
print(s.check_if_displayed('/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr', 'No Records Found'))

# finishing to avoid many windows
s.finish()