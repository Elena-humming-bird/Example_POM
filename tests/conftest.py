import pytest
from selenium import webdriver

import data
from pages.auth_page import AuthPage
from locators import AuthLocators
from data import auth_url, username, password


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def auth(driver):
    page = AuthPage(driver, data.auth_url)
    page.open()
    page.field_user_name().send_keys(username)
    page.field_password().send_keys(password)
    page.btn_login().click()
