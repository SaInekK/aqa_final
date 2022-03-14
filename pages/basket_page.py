from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_adding_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_STRONG_NAME), (
            "Adding message is not presented")

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.BASKET_STRONG_NAME).text
        assert product_name == message_text, "Product name != name in the message"

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_price_in_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE).text
        assert product_price == basket_total_price_message, "No product price in the message"

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "There are items in basket"
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), "Empty basket message is not presented"
