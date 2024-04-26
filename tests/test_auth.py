import data
from pages.auth_page import AuthPage, InventoryPage

from locators import AuthLocators
from data import *


def test_title(driver):
    driver.get(auth_url)
    assert driver.title == title


def test_auth_positive(driver):
    login_page = AuthPage(driver, data.auth_url)
    login_page.open()

    # 1 version
    # login_page.find_el(AuthLocators.FIELD_USER_NAME).send_keys(username)
    # 2 version
    login_page.field_user_name().send_keys(username)

    login_page.field_password().send_keys(password)
    login_page.btn_login().click()
    assert driver.current_url == inventory_url, 'URL does not match'

    # 1 version
    assert login_page.find_el(InventoryPage.LABEL_PRODUCTS).text == 'Products'
    # 2 version
    # assert driver.find_element(*InventoryPage.LABEL_PRODUCTS).text == 'Products'


def test_auth_negative(driver):
    login_page = AuthPage(driver, data.auth_url)
    login_page.open()

    login_page.field_user_name().send_keys('user')
    login_page.field_password().send_keys('user')
    login_page.btn_login().click()

    assert login_page.find_el(AuthLocators.BTN_ERROR), 'No such element'
    assert driver.find_element(AuthLocators.BTN_ERROR).text == login_error_message, "No such message"
