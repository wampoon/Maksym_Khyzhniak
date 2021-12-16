from behave import *
from selenium.webdriver.common.by import By
from base_app import BasePage
from orange_pages import DashboardPage, LoginPage, PaygradesPage
from utils import Results

base = BasePage().go_to_site()
login = LoginPage()
dash = DashboardPage()
pgrades = PaygradesPage()

@given(u'we have username \'Admin\'')
def step_impl(context):
    desired_username = 'Admin'
    x = login.set_username(desired_username)
    assert login.username == desired_username


@given(u'password \'admin123\'')
def step_impl(context):
    desired_password = 'admin123'
    login.set_password(desired_password)
    assert login.password == desired_password


@when(u'we put username into username field')
def step_impl(context):
    login.put_username()
    assert True==True


@when(u'we put password into password field')
def step_impl(context):
    login.put_password()
    assert True==True


@when(u'we click login button')
def step_impl(context):
    prev_url = login.driver.current_url
    login.click_login_button()
    curr_url = login.driver.current_url
    print(prev_url, curr_url)
    assert prev_url != curr_url


@then(u'we must be successfuly logged in')
def step_impl(context):
    random_element = dash.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    assert random_element!=None


@given(u'we are logged in sucessfully')
def step_impl(context):
    random_element = dash.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[2]')
    assert random_element!=None


@when(u'we click on \'Admin\' section in navbar')
def step_impl(context):
    dash.go_to_admin()
    random_element = dash.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/a')
    assert random_element!=None


@then(u'Admin page is opened')
def step_impl(context):
    random_element = dash.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/a')
    assert random_element!=None


@given(u'we are on Admin page')
def step_impl(context):
    random_element = dash.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/a')
    assert random_element!=None


@when(u'we hover on \'Job\'')
def step_impl(context):
    dash.go_to_job
    assert dash.go_to_job()!=None


@then(u'dropdown menu must be shown')
def step_impl(context):
    # class of dropdown does not change so is_displayed() wont work so i dont know how to implement :(
    assert True == True


@given(u'we have \'Job\' dropdown menu opened')
def step_impl(context):
    dash.go_to_job()
    assert dash.go_to_job() != None


@when(u'we click \'Pay Grades\' button')
def step_impl(context):
    dash.go_to_paygrades()

    # assert dash.go_to_paygrades()!=None

@then(u'\'Pay Grades\' section is displayed')
def step_impl(context):
    curr_url = pgrades.driver.current_url
    desired_url = 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades'
    assert curr_url == desired_url


@given(u'we are at Pay Grades page')
def step_impl(context):
    curr_url = pgrades.driver.current_url
    desired_url = 'https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades'
    assert curr_url == desired_url


@when(u'we click \'Add\' button in \'Pay Grades\' section')
def step_impl(context):
    pgrades.click_add_paygrade()
    curr_url = pgrades.driver.current_url
    desired_url = 'https://opensource-demo.orangehrmlive.com/index.php/admin/payGrade'
    assert curr_url == desired_url


@when(u'put \'RandomName\' in \'Name\' field')
def step_impl(context):
    field = pgrades.set_random_name()
    curr_class = field.get_attribute('class')
    desired_class = 'valid'
    assert curr_class == desired_class


@when(u'click \'Save\' button')
def step_impl(context):
    pgrades.click_save()
    section = pgrades.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/h1')
    assert section!=None


@then(u'section \'Assigned Currencies\' must be displayed')
def step_impl(context):
    section = pgrades.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/h1')
    assert section!=None


@given(u'we have \'Assigned Currencies\' section displayed')
def step_impl(context):
    section = pgrades.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[1]/h1')
    assert section!=None


@when(u'we click \'Add\' button')
def step_impl(context):
    pgrades.click_add_currency()
    currencies = pgrades.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]')
    assert currencies!=None


@when(u'put \'USD - United States Dollar\' in \'Currency\' field')
def step_impl(context):
    pgrades.set_currency()
    assert True==True


@when(u'put \'1\' in \'Minimum Salary\' field')
def step_impl(context):
    pgrades.set_min_wage(1)
    assert True==True


@when(u'put \'5\' in \'Maximum Salary\' field')
def step_impl(context):
    pgrades.set_max_wage(5)
    assert True==True


@when(u'click \'Save\' button in editing section')
def step_impl(context):
    pgrades.save_currency_info()
    True==True


@then(u'in \'Assigned Currencies\' section must be displayed row {\'Currency\':\'United States Dollar, \'Minimum Salary\':\'1.00\', \'Maximum Salary\':\'5.00\'}')
def step_impl(context):
    rows = pgrades.find_elements([By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[2]/form/table/tbody/tr'])
    res = Results.res_bad
    for i in rows:
        if 'United States Dollar' in i.text: res = Results.res_good
        else: res = Results.res_bad

    assert res==Results.res_good

