from controller import *
import uuid


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
