import random
import string
import time

import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import faker


def generate_email():
    f = faker.Faker()
    email = f.email()
    return email


def generate_password(password_length=9):
    temp = random.choices(string.ascii_letters, k=password_length)
    password = ''.join(temp)
    return password


@pytest.mark.need_review
@pytest.mark.parametrize('number', [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, number):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_adding_message()
    page.should_be_price_in_basket_total_message()
    # time.sleep(5)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_url = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        self.login_page = LoginPage(browser, login_url)
        self.login_page.open()
        self.login_page.register_new_user(generate_email(), generate_password())
        self.login_page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.xfail(reason='bugged')
    # @pytest.mark.parametrize('number', [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_adding_message()
        page.should_be_price_in_basket_total_message()
        # time.sleep(5)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail(reason="there is message after adding")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="message after adding isnt disappearing")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.element_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
