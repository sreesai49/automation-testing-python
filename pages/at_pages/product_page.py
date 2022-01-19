import allure

from base.page_base import PageBase
from locators.at_locators import ProductPageLocators, BasketPageLocators
from utils.driver_helper import DriverHelper


class ProductPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        global driver_helper
        driver_helper = DriverHelper(self.driver)

    @allure.step("Click add to basket button")
    def click_add_to_basket(self):
        driver_helper.wait_till_element_visible(*ProductPageLocators.add_to_basket)
        driver_helper.click_element(*ProductPageLocators.add_to_basket)

    @allure.step("Get success message")
    def get_success_message(self):
        driver_helper.wait_till_element_visible(*ProductPageLocators.success_message)
        return driver_helper.get_attribute_text(*ProductPageLocators.success_message, "text")

    @allure.step("Click on basket price menu")
    def click_basket_price(self):
        driver_helper.wait_till_element_visible(*ProductPageLocators.basket_price)
        driver_helper.click_element(*ProductPageLocators.basket_price)
        driver_helper.wait_till_element_visible(*BasketPageLocators.product_name)

    @allure.step("Click description tab in product page")
    def click_description_tab(self):
        driver_helper.scroll_to_element(*ProductPageLocators.description_tab, 2)
        driver_helper.click_element(*ProductPageLocators.description_tab)

    @allure.step("Get product name from product page")
    def get_product_name(self):
        return driver_helper.get_attribute_text(*ProductPageLocators.product_title, "text")

    @allure.step("Get product description text from product page")
    def get_description(self):
        return driver_helper.get_attribute_text(*ProductPageLocators.description, "text")

    @allure.step("Click reviews tab")
    def click_reviews_tab(self):
        driver_helper.scroll_to_element(*ProductPageLocators.reviews_tab, 2)
        driver_helper.click_element(*ProductPageLocators.reviews_tab)

    @allure.step("Get reviews reply title text")
    def get_review_reply_title(self):
        return driver_helper.get_attribute_text(*ProductPageLocators.review_reply_title, "text")

    @allure.step("Get basket price")
    def get_basket_price(self):
        price_text = driver_helper.get_attribute_text(*ProductPageLocators.basket_price, "text")
        actual_price = price_text.split(".")[0]
        num = ""
        for c in actual_price:
            if c.isdigit():
                num = num + c
        return int(num)

    @allure.step("Get product price")
    def get_product_price(self):
        price_text = driver_helper.get_attribute_text(*ProductPageLocators.product_price, "text")
        actual_price = price_text.split(".")[0]
        num = ""
        for c in actual_price:
            if c.isdigit():
                num = num + c
        return int(num)

    @allure.step("Get product stock")
    def get_product_stock(self):
        stock = driver_helper.get_attribute_text(*ProductPageLocators.product_stock, "text")
        return int(stock.split()[0])

    @allure.step("Get error message")
    def get_error_message(self):
        driver_helper.wait_till_element_visible(*ProductPageLocators.error_message)
        return driver_helper.get_attribute_text(*ProductPageLocators.error_message, "text")