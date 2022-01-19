import allure
import pytest

from pages.at_pages.basket_page import BasketPage
from pages.at_pages.home_page import HomePage
from pages.at_pages.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @allure.title("Home page with three sliders only")
    @allure.description("1) Open the browser\n"+
            "2) Enter the URL “http://practice.automationtesting.in/”\n"+
            "3) Click on Shop Menu\n"+
            "4) Now click on Home menu button\n"+
            "5) Test whether the Home page has Three Sliders only\n"+
            "6) The Home page must contains only three sliders")
    def test1_homepage_with_three_sliders_only(self):
        global homepage
        homepage = HomePage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        sliders_set = homepage.test_whether_home_page_has_three_sliders_only()
        assert len(sliders_set) == 3

    @allure.title("Home page with three Arrivals only")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals")
    def test2_homepage_with_three_arrivals_only(self):
        homepage = HomePage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

    @allure.title("Home page - Images in arrivals should navigate")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n"+
                        "7) Now click the image in the Arrivals\n"+
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n"+
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket")
    def test3_homepage_images_in_arrivals_should_navigate(self):
        homepage = HomePage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3
        homepage.open_selenium_ruby_arrival_add_to_basket()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        homepage.open_html_arrival_add_to_basket()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        homepage.open_javascript_arrival_add_to_basket()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        global productpage
        productpage = ProductPage(self.driver)
        productpage.click_basket_price()
        BasketPage(self.driver).verify_items_in_basket_page()

    @allure.title("Home page - Arrivals-Images-Description")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n"+
                        "10) Click on Description tab for the book you clicked on.\n"+
                        "11) There should be a description regarding that book the user clicked on")
    def test4_homepage_arrivals_images_description(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        homepage.open_selenium_ruby_arrival_add_to_basket()
        product_name = productpage.get_product_name().split()[0]
        productpage.click_description_tab()
        assert product_name in productpage.get_description()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        homepage.open_html_arrival_add_to_basket()
        product_name = productpage.get_product_name().split()[2]
        productpage.click_description_tab()
        assert product_name in productpage.get_description()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        homepage.open_javascript_arrival_add_to_basket()
        product_name = productpage.get_product_name().split()[1]
        productpage.click_description_tab()
        assert product_name in productpage.get_description()
        productpage.click_basket_price()
        BasketPage(self.driver).verify_items_in_basket_page()

    @allure.title("Home page - Arrivals-Images-Reviews")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Now clock on Reviews tab for the book you clicked on.\n" +
                        "11) There should be a Reviews regarding that book the user clicked on")
    def test5_homepage_arrivals_images_reviews(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        homepage.open_selenium_ruby_arrival_add_to_basket()
        product_name = productpage.get_product_name()
        productpage.click_reviews_tab()
        assert product_name in productpage.get_review_reply_title()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        homepage.open_html_arrival_add_to_basket()
        product_name = productpage.get_product_name()
        productpage.click_reviews_tab()
        assert product_name in productpage.get_review_reply_title()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        homepage.open_javascript_arrival_add_to_basket()
        product_name = productpage.get_product_name()
        productpage.click_reviews_tab()
        assert product_name in productpage.get_review_reply_title()
        productpage.click_basket_price()
        BasketPage(self.driver).verify_items_in_basket_page()

    @allure.title("Home page - Arrivals-Images-Add to Basket")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Click on the Add To Basket button which adds that book to your basket\n" +
                        "11) User can view that Book in the Menu item with price.\n"+
                        "12) User can add a book by clicking on Add To Basket button which adds that book in to his Basket")
    def test6_homepage_arrivals_images_add_to_basket(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        basketpage = BasketPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        basket_price = productpage.get_basket_price()
        homepage.open_selenium_ruby_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items, True
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_html_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items, True
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_javascript_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items, True
        productpage.click_basket_price()
        BasketPage(self.driver).verify_items_in_basket_page()

    @allure.title("Home page - Arrivals-Add to Basket with more books")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Click on the Add To Basket button which adds that book to your basket\n" +
                        "11) User can view that Book in the Menu item with price.\n" +
                        "12) User can add a book by clicking on Add To Basket button which adds that book in to his Basket\n"+
                        "13) Select more books than the books in stock.Ex if the stock has 20 books, try to add 21.\n"+
                        "14) Click the add to basket button\n"
                        "15) Now it throws an error prompt like you must enter a value between 1 and 20")
    def test7_homepage_arrivals_add_to_basket_with_more_books(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        basketpage = BasketPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        basket_price = productpage.get_basket_price()
        homepage.open_selenium_ruby_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        product_stock = productpage.get_product_stock()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        basketpage.update_quantity(product_stock)
        basketpage.click_update_basket_button()

        assert basketpage.get_basket_items_count() == product_stock
        basketpage.click_product_name()
        productpage.click_add_to_basket()
        error_message = productpage.get_error_message().split("\n")[1]
        assert error_message == "You cannot add that amount to the cart — we have "+\
                              str(product_stock)+" in stock and you already have "+str(product_stock)+" in your cart."
        productpage.click_basket_price()
        basketpage.click_remove_button()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_html_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        product_stock = productpage.get_product_stock()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        basketpage.update_quantity(product_stock)
        basketpage.click_update_basket_button()
        basketpage.click_product_name()
        productpage.click_add_to_basket()
        error_message = productpage.get_error_message().split("\n")[1]
        assert error_message == "You cannot add that amount to the cart — we have " + \
               str(product_stock) + " in stock and you already have " + str(product_stock) + " in your cart."
        productpage.click_basket_price()
        basketpage.click_remove_button()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_javascript_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        product_stock = productpage.get_product_stock()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        basketpage.update_quantity(product_stock)
        basketpage.click_update_basket_button()
        basketpage.click_product_name()
        productpage.click_add_to_basket()
        error_message = productpage.get_error_message().split("\n")[1]
        assert error_message == "You cannot add that amount to the cart — we have " + \
               str(product_stock) + " in stock and you already have " + str(product_stock) + " in your cart."
        productpage.click_basket_price()
        basketpage.click_remove_button()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

    @allure.title("Home page - Arrivals-Add to Basket-Items")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Click on the Add To Basket button which adds that book to your basket\n" +
                        "11) User can view that Book in the Menu item with price.\n" +
                        "12) Now click on Item link which navigates to proceed to check out page.\n"+
                        "13) User can click on the Item link in menu item after adding the book in to the basket which leads to the check out page")
    def test8_homepage_arrivals_add_to_basket_items(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        basketpage = BasketPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        basket_price = productpage.get_basket_price()
        homepage.open_selenium_ruby_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_html_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_javascript_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        productpage.click_basket_price()
        BasketPage(self.driver).verify_items_in_basket_page()

    @allure.title("Home page - Arrivals-Add to Basket-Items-Coupon")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Click on the Add To Basket button which adds that book to your basket\n" +
                        "11) User can view that Book in the Menu item with price.\n" +
                        "12) Now click on Item link which navigates to proceed to check out page.\n" +
                        "13) User can click on the Item link in menu item after adding the book in to the basket which leads to the check out page\n"+
                        "14) Enter the Coupon code as ‘krishnasakinala’ to get 50rps off on the total.\n"+
                        "15) User can able to apply coupon by entering ‘krishnasakinala’ in the coupon textbox which give 50rps off on the total price")
    def test9_homepage_arrivals_add_to_basket_items_coupon(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        basketpage = BasketPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        basket_price = productpage.get_basket_price()
        homepage.open_selenium_ruby_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_html_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_javascript_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        productpage.click_basket_price()
        basketpage.verify_items_in_basket_page()
        basketpage.enter_coupon_code("krishnasakinala")
        basketpage.click_apply_coupon_button()
        basketpage.validate_applied_coupon("krishnasakinala", "₹50.00")

    @allure.title("Home page - Arrivals-Add to Basket-Items-Coupon value<450")
    @allure.description("1) Open the browser\n" +
                        "2) Enter the URL “http://practice.automationtesting.in/”\n" +
                        "3) Click on Shop Menu\n" +
                        "4) Now click on Home menu button\n" +
                        "5) Test whether the Home page has Three Arrivals only\n" +
                        "6) The Home page must contains only three Arrivals\n" +
                        "7) Now click the image in the Arrivals\n" +
                        "8) Test whether it is navigating to next page where the user can add that book into his basket.\n" +
                        "9) Image should be clickable and should navigate to next page where user can add that book to his basket\n" +
                        "10) Click on the Add To Basket button which adds that book to your basket\n" +
                        "11) User can view that Book in the Menu item with price.\n" +
                        "12) Now click on Item link which navigates to proceed to check out page.\n" +
                        "13) User can click on the Item link in menu item after adding the book in to the basket which leads to the check out page\n" +
                        "14) Enter the Coupon code as ‘krishnasakinala’ to get 50rps off on the total.\n" +
                        "15) User can able to apply coupon by entering ‘krishnasakinala’ in the coupon textbox which give 50rps off on the total price"+
                        "because the coupon is applicable for the book price > 450 rps")
    def test10_homepage_arrivals_add_to_basket_items_coupon_value_below_450(self):
        homepage = HomePage(self.driver)
        productpage = ProductPage(self.driver)
        basketpage = BasketPage(self.driver)
        homepage.open()
        homepage.click_on_shop_menu()
        homepage.click_on_home_menu_button()
        homepage.scroll_to_arrivals_images()
        arrivals_count = homepage.get_arrivals_count()
        assert arrivals_count == 3

        basket_price = productpage.get_basket_price()
        homepage.open_selenium_ruby_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        basketpage.click_remove_button()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_html_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        basketpage.click_remove_button()
        homepage.click_site_logo()
        homepage.scroll_to_arrivals_images()

        basket_price = productpage.get_basket_price()
        homepage.open_javascript_arrival_add_to_basket()
        assert basket_price + productpage.get_product_price() == productpage.get_basket_price()
        product_name = productpage.get_product_name()
        productpage.click_basket_price()
        basket_items = basketpage.get_basket_items()
        assert product_name in basket_items
        productpage.click_basket_price()
        basketpage.enter_coupon_code("krishnasakinala")
        basketpage.click_apply_coupon_button()
        assert basketpage.get_error_message()=="The minimum spend for this coupon is ₹450.00."