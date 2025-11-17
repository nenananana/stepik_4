from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()

        self.should_be_success_message()
        self.should_be_correct_product_name(product_name)
        self.should_be_basket_total()
        self.should_be_correct_price(product_price)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_correct_product_name(self, product_name):
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, f"Product name in message doesn't match. Expected: {product_name}, got: {message_product_name}"

    def should_be_basket_total(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE), "Basket total message is not presented"

    def should_be_correct_price(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Price in basket doesn't match product price. Expected: {product_price}, got: {basket_total}"