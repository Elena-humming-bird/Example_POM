# импортируем функции для всех страниц (импортируем родительский класс)
from pages.main_page import BasePage
# импортируем только нужные локаторы
from locators import AuthLocators, InventoryPage


class AuthPage(BasePage):

    def field_user_name(self):
        return self.is_visible(AuthLocators.FIELD_USER_NAME)

    def field_password(self):
        return self.is_visible(AuthLocators.FIELD_PASSWORD)

    def btn_login(self):
        return self.is_clickable(AuthLocators.BTN_LOGIN)

    def btn_error(self):
        return self.is_clickable(AuthLocators.BTN_ERROR)