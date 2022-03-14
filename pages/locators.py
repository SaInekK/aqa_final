from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > .btn-group > a.btn-default")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_FORM_PASS1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_FORM_PASS2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    BASKET_STRONG_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main >.price_color")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
