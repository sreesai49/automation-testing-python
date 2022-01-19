from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from base.page_base import PageBase


class DriverHelper(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_till_element_visible(self, locator_type, locator_strategy):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        return WebDriverWait(self.driver, 15, ignored_exceptions=ignored_exceptions).\
            until(EC.visibility_of_element_located((locator_type, locator_strategy)))

    def click_element(self, locator_type, locator_strategy):
        try:
            self.driver.find_element(locator_type, locator_strategy).click()
        except StaleElementReferenceException:
            print("StaleElementReferenceException occured")

    def get_attribute_text(self, locator_type, locator_strategy, attribute_name):
        if attribute_name == "text":
            return self.driver.find_element(locator_type, locator_strategy).text
        else:
            return self.driver.find_element(locator_type, locator_strategy).get_attribute(attribute_name)

    def is_element_present(self, locator_type, locator_strategy):
        try:
            flag = self.driver.find_element(locator_type, locator_strategy).is_displayed()
        except:
            flag = False
        return flag

    def scroll_to_element(self, locator_type, locator_strategy, scroll_count):
        if self.is_element_present(locator_type, locator_strategy):
            element = self.driver.find_element(locator_type, locator_strategy)
            desired_y = (element.size['height'] / 2) + element.location['y']
            current_y = (self.driver.execute_script('return window.innerHeight') / 2) + self.driver.execute_script(
                'return window.pageYOffset')
            scroll_y_by = desired_y - current_y
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        else:
            while(scroll_count > 0):
                if self.is_element_present(locator_type, locator_strategy):
                    break
                else:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.25);")
                scroll_count = scroll_count-1;