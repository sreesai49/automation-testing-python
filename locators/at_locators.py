from selenium.webdriver.common.by import By


class HomePageLocators:
    shop_menu = (By.XPATH, "//ul[@id='main-nav']/li[1]")
    home_menu = (By.XPATH, "//a[text()='Home']")
    sliders = (By.XPATH, "//*[@class='n2-ss-slide-background']")
    slider_image = (By.XPATH, "//*[contains(@class, 'n2-ss-slide-active')]//img")
    left_arrow = (By.XPATH, "(//*[@class='n2-ow'])[1]")
    right_arrow = (By.XPATH, "(//*[@class='n2-ow'])[2]")
    site_logo = (By.ID, "site-logo")
    arrivals_images = (By.XPATH, "//*[@class='woocommerce-LoopProduct-link']/img")
    new_arrivals_link = (By.TAG_NAME, "h2")

class ProductPageLocators:
    product_title = (By.XPATH, "//*[@class='product_title entry-title']")
    add_to_basket = (By.XPATH, "//button[@type='submit']")
    success_message = (By.XPATH, "//*[@class='woocommerce-message']")
    basket_price = (By.XPATH, "//*[@class='amount']")
    description_tab= (By.XPATH, "//*[contains(@class, 'description_tab')]")
    reviews_tab = (By.XPATH, "//*[contains(@class, 'reviews_tab')]")
    description = (By.XPATH, "//*[@id='tab-description']//p")
    review_reply_title = (By.ID, "reply-title")
    product_price = (By.XPATH, "(//*[@class='summary entry-summary']//*[@class='woocommerce-Price-amount amount'])[last()]")
    product_stock = (By.XPATH, "//*[@class='stock in-stock']")
    error_message = (By.XPATH, "//*[@class='woocommerce-error']")

class BasketPageLocators:
    product_name = (By.XPATH, "//*[@class='product-name']//a")
    quantity = (By.XPATH, "//*[@class='quantity']/input")
    remove_button = (By.XPATH, "//*[@class='product-remove']/a")
    update_basket_button = (By.XPATH, "//*[@name='update_cart']")
    basket_items_count = (By.XPATH, "//*[@class='cartcontents']")
    success_message = (By.XPATH, "//*[@class='woocommerce-message']")
    coupon_field = (By.ID, "coupon_code")
    apply_coupon_button = (By.XPATH, "//*[@name='apply_coupon']")
    applied_coupon_title = (By.XPATH, "//*[contains(@class, 'cart-discount')]/th")
    applied_coupon_data = (By.XPATH, "//*[contains(@class, 'cart-discount')]/td")
    error_message = (By.XPATH, "//*[@class='woocommerce-error']")


