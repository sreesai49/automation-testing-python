from time import sleep

import allure

from base.page_base import PageBase
from locators.at_locators import BasketPageLocators
from pages.at_pages.product_page import ProductPage
from utils.driver_helper import DriverHelper


class BasketPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        global driver_helper
        driver_helper = DriverHelper(self.driver)

    @allure.step("Verify all three books added to basket items list")
    def verify_items_in_basket_page(self):
        elements = self.driver.find_elements(*BasketPageLocators.product_name)
        assert len(elements) == 3

    @allure.step("Get basket items list")
    def get_basket_items(self):
        basket_items = []
        elements = self.driver.find_elements(*BasketPageLocators.product_name)
        for element in elements:
            basket_items.append(element.text)
        return basket_items

    @allure.step("Click remove button in basket screen")
    def click_remove_button(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.remove_button)
        driver_helper.click_element(*BasketPageLocators.remove_button)

    @allure.step("Update item quantity")
    def update_quantity(self, quantity):
        driver_helper.wait_till_element_visible(*BasketPageLocators.quantity)
        self.driver.find_element(*BasketPageLocators.quantity).clear()
        self.driver.find_element(*BasketPageLocators.quantity).send_keys(quantity)

    @allure.step("Click update basket button")
    def click_update_basket_button(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.update_basket_button)
        driver_helper.click_element(*BasketPageLocators.update_basket_button)
        sleep(5)
        driver_helper.wait_till_element_visible(*BasketPageLocators.success_message)

    @allure.step("Click product name in basket page")
    def click_product_name(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.product_name)
        driver_helper.click_element(*BasketPageLocators.product_name)

    @allure.step("Get basket items count")
    def get_basket_items_count(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.basket_items_count)
        count = driver_helper.get_attribute_text(*BasketPageLocators.basket_items_count, "text")
        return int(count.split()[0])

    @allure.step("Enter coupon code in field")
    def enter_coupon_code(self, coupon_code):
        driver_helper.wait_till_element_visible(*BasketPageLocators.coupon_field)
        self.driver.find_element(*BasketPageLocators.coupon_field).send_keys(coupon_code)

    @allure.step("Click Apply coupon button")
    def click_apply_coupon_button(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.apply_coupon_button)
        driver_helper.click_element(*BasketPageLocators.apply_coupon_button)

    @allure.step("validate applied coupon text")
    def validate_applied_coupon(self, coupon_code, discount_value):
        driver_helper.scroll_to_element(*BasketPageLocators.applied_coupon_title, 2)
        driver_helper.wait_till_element_visible(*BasketPageLocators.applied_coupon_title)
        coupon_text = driver_helper.get_attribute_text(*BasketPageLocators.applied_coupon_title, "text")
        coupon_value = driver_helper.get_attribute_text(*BasketPageLocators.applied_coupon_data, "text")
        assert coupon_code in coupon_value
        assert discount_value in coupon_text

    @allure.step("Get error message")
    def get_error_message(self):
        driver_helper.wait_till_element_visible(*BasketPageLocators.error_message)
        return driver_helper.get_attribute_text(*BasketPageLocators.error_message, "text")