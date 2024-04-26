class AuthLocators:
    FIELD_USER_NAME = ("xpath", "//*[@id='user-name']")
    FIELD_PASSWORD = ("xpath", "//*[@id='password']")
    BTN_LOGIN = ("xpath", "//*[@id='login-button']")
    BTN_ERROR = ("xpath", '//*[@data-test="error"]')


class InventoryPage:
    LABEL_PRODUCTS = ("xpath", '//*[@class="product_label"]')
    item_name = ("xpath", '(//*[@class ="inventory_item_name"])')
    item_img = ("xpath", '(//*[@class="inventory_item_img"])')
    item_price = ("xpath", '//*[@class="inventory_item_price"]')
    add_to_cart_button = ("xpath", '(//*[@class="btn_primary btn_inventory"])')
    remove_btn_inventory = ("xpath", '(//*[@class="btn_secondary btn_inventory"])')
    basket_icon = ("xpath", '//*[@ fill = "currentColor"]')
    filter_dropdown = ("xpath", '//*[@class="product_sort_container"]')


class CartLocators:
    remove_btn_basket = ("xpath", '//*[@class="btn_secondary cart_button"]')
    items_in_basket = ('xpath', '//div[@class="cart_item"]')


class ItemCartLocators:
    inventory_details_img = ("xpath", '//*[@class ="inventory_details_img"]')
    inventory_details_name = ("xpath", '//*[@class="inventory_details_name"]')
    inventory_details_desc = ("xpath", '//*[@class="inventory_details_desc"]')
    inventory_details_price = ("xpath", '//*[@class="inventory_details_price"]')
    inventory_details_back_btn = ("xpath", '//*[@class="inventory_details_back_button"]')


class OrderLocators:
    checkout_btn = ("xpath", '//*[@class="btn_action checkout_button"]')
    first_name_field = ("xpath", "//*[@id='first-name']")
    last_name_field = ("xpath", "//*[@id='last-name']")
    postcode_field = ("xpath", "//*[@id='postal-code']")
    continue_btn = ("xpath", "//*[@class='btn_primary cart_button']")
    finish_btn = ("xpath", '//*[@class="btn_action cart_button"]')


class BurgerMenuLocators:
    burger_menu_btn = ("xpath", '//*[@class="bm-burger-button"]')
    all_items_btn = ("xpath", '//*[@id="inventory_sidebar_link"]')
    about_btn = ("xpath", '//*[@id="about_sidebar_link"]')
    logout_btn = ("xpath", '//*[@id="logout_sidebar_link"]')
    reset_app_state_btn = ("xpath", '//*[@id="reset_sidebar_link"]')



