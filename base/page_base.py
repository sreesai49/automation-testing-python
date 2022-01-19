import allure


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Enter the URL “http://practice.automationtesting.in/”")
    def open(self):
        self.driver.open()
        self.driver.maximize_window()
