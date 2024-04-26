# импортируем функции для всех страниц (импортируем родительский класс)
from pages.main_page import BasePage
# импортируем только нужные локаторы
from locators import InventoryPage


class AuthPage(BasePage):

    def label_products(self):
        return self.is_visible(InventoryPage.LABEL_PRODUCTS)