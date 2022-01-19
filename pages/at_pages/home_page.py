import allure

from base.page_base import PageBase
from locators.at_locators import HomePageLocators, ProductPageLocators
from pages.at_pages.product_page import ProductPage
from utils.driver_helper import DriverHelper
from selenium.common.exceptions import StaleElementReferenceException


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        global driver_helper, product_page
        driver_helper = DriverHelper(self.driver)
        product_page = ProductPage(self.driver)

    @allure.step("Click on Shop Menu")
    def click_on_shop_menu(self):
        driver_helper.wait_till_element_visible(*HomePageLocators.shop_menu)
        driver_helper.click_element(*HomePageLocators.shop_menu)

    @allure.step("Now click on Home menu button")
    def click_on_home_menu_button(self):
        driver_helper.wait_till_element_visible(*HomePageLocators.home_menu)
        driver_helper.click_element(*HomePageLocators.home_menu)

    @allure.step("Test whether the Home page has Three Sliders only")
    def test_whether_home_page_has_three_sliders_only(self):
        driver_helper.wait_till_element_visible(*HomePageLocators.slider_image)
        elements = self.driver.find_elements(*HomePageLocators.sliders)
        list = []
        for element in elements:
            list.append(driver_helper.get_attribute_text(*HomePageLocators.slider_image, "src"))
            driver_helper.click_element(*HomePageLocators.right_arrow)
            driver_helper.wait_till_element_visible(*HomePageLocators.slider_image)
        all_sliders = set(list)
        return all_sliders

    @allure.step("Click on site logo")
    def click_site_logo(self):
        driver_helper.wait_till_element_visible(*HomePageLocators.site_logo)
        driver_helper.click_element(*HomePageLocators.site_logo)

    @allure.step("Scroll to arrivals images")
    def scroll_to_arrivals_images(self):
        driver_helper.scroll_to_element(*HomePageLocators.arrivals_images, 2)
        assert driver_helper.is_element_present(*HomePageLocators.new_arrivals_link) == True

    @allure.step("Get new arrivals count from home screen")
    def get_arrivals_count(self):
        driver_helper.wait_till_element_visible(*HomePageLocators.arrivals_images)
        elements = self.driver.find_elements(*HomePageLocators.arrivals_images)
        return len(elements)

    @allure.step("Open Selenium ryby book and add to basket")
    def open_selenium_ruby_arrival_add_to_basket(self):
        try:
            self.driver.find_elements(*HomePageLocators.arrivals_images)[0].click()
        except:
            print("StaleElementReferenceException occured")
        driver_helper.wait_till_element_visible(*ProductPageLocators.product_title)
        product_page.click_add_to_basket()
        actual_message = product_page.get_success_message().split("\n")[1]
        expected_message = "“" + driver_helper.get_attribute_text(*ProductPageLocators.product_title, "text") + "” has been added to your basket."
        assert actual_message == expected_message

    @allure.step("Open html book and add to basket")
    def open_html_arrival_add_to_basket(self):
        try:
            self.driver.find_elements(*HomePageLocators.arrivals_images)[1].click()
        except:
            print("StaleElementReferenceException occured")
        driver_helper.wait_till_element_visible(*ProductPageLocators.product_title)
        product_page.click_add_to_basket()
        actual_message = product_page.get_success_message().split("\n")[1]
        expected_message = "“" + driver_helper.get_attribute_text(*ProductPageLocators.product_title, "text") + "” has been added to your basket."
        assert actual_message == expected_message

    @allure.step("Open javascript book and add to basket")
    def open_javascript_arrival_add_to_basket(self):
        try:
            self.driver.find_elements(*HomePageLocators.arrivals_images)[2].click()
        except:
            print("StaleElementReferenceException occured")
        driver_helper.wait_till_element_visible(*ProductPageLocators.product_title)
        product_page.click_add_to_basket()
        actual_message = product_page.get_success_message().split("\n")[1]
        expected_message = "“" + driver_helper.get_attribute_text(*ProductPageLocators.product_title, "text") + "” has been added to your basket."
        assert actual_message == expected_message