from selenium.webdriver.common import by
from base_app import BasePage
from selenium.webdriver.common.by import By
import uuid

class Locators:
    USERNAME_INPUT_FIELD = [By.ID, "txtUsername"]
    PASSWORD_INPUT_FIELD = [By.ID, "txtPassword"]
    LOGIN_BTN = [By.XPATH, '//*[@id="btnLogin"]']
    ADMIN_NAVBAR_BTN = [By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/a']
    JOB_NAVBAR_BTN = [By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]']
    PAYGRADES_NAVBAR_BTN = [By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a']
    ADD_PAYGRADES_BTN = [By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]']
    NEW_PAYGRADE_NAME_INPUT = [By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/input[1]']
    NEW_PAYGRADE_SAVE_BTN = [By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]']
    ADD_CURRENCY_BTN = [By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input']
    CURRENCY_CURRENCY_INPUT= [By.XPATH,'/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/input']
    CURRENCY_MINIMUM_INPUT = [By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input']
    CURRENCY_MAXIMUM_INPUT = [By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input']
    CURRENCY_SAVE_BTN = [By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/p/input[1]']
    NEW_CURRENCY_ROW = [By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr']
    NEW_CURRENCY_CHECKBOX = [By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr/td[1]/input']
    CURRENCY_DELETE_BTN = [By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input[2]']


class LoginPage(BasePage):
    username = None
    password = None

    def set_username(self, username):
        self.username = username
        
    def set_password(self, password):
        self.password = password

    def put_username(self):
        username_field = self.find_element(Locators.USERNAME_INPUT_FIELD)
        username_field.click()
        username_field.send_keys(self.username)

    def put_password(self):
        password_field = self.find_element(Locators.PASSWORD_INPUT_FIELD)
        password_field.click()
        password_field.send_keys(self.password)

    def click_login_button(self):
        login_btn = self.find_element(Locators.LOGIN_BTN)
        login_btn.click()
        return login_btn

        
class DashboardPage(BasePage):

    def go_to_admin(self):
        admin_btn = self.find_element(Locators.ADMIN_NAVBAR_BTN)
        admin_btn.click()
        return admin_btn

    def go_to_job(self):
        job_btn = self.find_element(Locators.JOB_NAVBAR_BTN)
        job_btn.click()
        return job_btn

    def go_to_paygrades(self):
        paygrades_btn = self.find_element(Locators.PAYGRADES_NAVBAR_BTN)
        paygrades_btn.click()
        return paygrades_btn


class PaygradesPage(BasePage):

    def click_add_paygrade(self):
        add_paygrade = self.find_element(Locators.ADD_PAYGRADES_BTN)
        add_paygrade.click()
        return add_paygrade

    def set_random_name(self, name=uuid.uuid4().hex[:10]):
        name_field = self.find_element(Locators.NEW_PAYGRADE_NAME_INPUT)
        name_field.click()
        name_field.send_keys(name)
        return name_field
    
    def click_save(self):
        save_paygrade_btn = self.find_element(Locators.NEW_PAYGRADE_SAVE_BTN)
        save_paygrade_btn.click()
        return save_paygrade_btn

    def click_add_currency(self):
        add_currency_btn = self.find_element(Locators.ADD_CURRENCY_BTN)
        add_currency_btn.click()
        return add_currency_btn

    def set_currency(self, currency='USD - United States Dollar'):
        currency_name_input = self.find_element(Locators.CURRENCY_CURRENCY_INPUT)
        currency_name_input.click()
        currency_name_input.send_keys(currency)
        return currency_name_input

    def set_min_wage(self, val=0):
        min_wage_input = self.find_element(Locators.CURRENCY_MINIMUM_INPUT)
        min_wage_input.click()
        min_wage_input.send_keys(val)
        return min_wage_input

    def set_max_wage(self, val=100):
        max_wage_input = self.find_element(Locators.CURRENCY_MAXIMUM_INPUT)
        max_wage_input.click()
        max_wage_input.send_keys(val)
        return max_wage_input

    def save_currency_info(self):
        save_currency = self.find_element(Locators.CURRENCY_SAVE_BTN)
        save_currency.click()
        return save_currency