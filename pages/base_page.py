import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from .locators import ProductPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_adding_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_STRONG_NAME), (
            "Adding message is not presented")

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.BASKET_STRONG_NAME).text
        assert product_name == message_text, "Product name != name in the message"

    def should_be_price_in_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_price_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE).text
        assert product_price == basket_total_price_message, "No product price in the message"
