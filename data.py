from faker import Faker

title = 'Swag Labs'

''' URL '''

auth_url = 'https://www.saucedemo.com/v1/'
inventory_url = 'https://www.saucedemo.com/v1/inventory.html'
order_step1_url = 'https://www.saucedemo.com/v1/checkout-step-one.html'
order_step2_url = 'https://www.saucedemo.com/v1/checkout-step-two.html'
complete_order_url = 'https://www.saucedemo.com/v1/checkout-complete.html'
about_url = 'https://saucelabs.com/'

''' CREDENTIALS '''

username = 'standard_user'
password = 'secret_sauce'

''' MESSAGES'''

login_error_message = 'Epic sadface: Username and password do not match any user in this service'


def fake_data():
    faker = Faker()
    return faker.first_name(), faker.last_name(), faker.postcode()
