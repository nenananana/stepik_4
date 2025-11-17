from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()

    # Метод возвращает название товара со страницы
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Метод возвращает цену товара со страницы
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Проверка: название товара в сообщении совпадает с названием на странице
    def should_be_correct_product_added_message(self, product_name):
        added_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == added_product_name, \
            f"Product name mismatch! Page: {product_name}, Message: {added_product_name}"

    # Проверка: цена корзины совпадает с ценой товара
    def should_be_correct_basket_price(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Basket total mismatch! Product price: {product_price}, Basket total: {basket_total}"
