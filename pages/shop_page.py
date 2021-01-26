from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ShopPage(BasePage):
    dropdown_option = Find(
        by=By.CSS_SELECTOR,
        value="span[data-bind='text: title']"
    )
    search_results_info = Find(
        by=By.XPATH,
        value="//div[@class='searchAndSort-container']/div/h1[@class='head_section']"
    )
    actual_products_num_info = Find(
        by=By.XPATH,
        value="//div[@class='displayedProductCount col-xs-12']/p"
    )
    add_product_links = Finds(
        by=By.XPATH,
        value="//button/span[.='Add to bag']/.."
    )
    cart_icon = Find(
        by=By.CSS_SELECTOR,
        value="span[class='tigi-header__bag-icon__label']"
    )
    checkout_button = Find(by=By.XPATH, value="//a[.='Checkout']")

    def get_dropdown_option(self):
        wait(self.dropdown_option.is_displayed)
        return self.dropdown_option.text

    def get_search_results_product_num(self):
        WebDriverWait(self._driver, 10).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "span[data-bind='text: title']")
        ))
        wait(self.search_results_info.is_displayed)
        return self.search_results_info.text.split(sep=" ")[0]

    def click_buy_product_link(self, index):
        WebDriverWait(self._driver, 10).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "span[data-bind='text: title']")
        ))
        quantity = str(int(self.cart_icon.text) + 1)

        # WebDriverWait(self._driver, 10).until(ec.visibility_of_all_elements_located(
        #     (By.XPATH, "//button/span[.='Add to bag']/..")
        # ))
        self.add_product_links[index].click()
        WebDriverWait(self._driver, 10).until(ec.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span[class='tigi-header__bag-icon__label']"), quantity
        ))

    def click_cart_icon(self):
        wait(self.cart_icon.is_displayed)
        self.cart_icon.click()

    def click_checkout_button(self):
        url = self._driver.current_url
        wait(self.checkout_button.is_displayed)
        self.checkout_button.click()
        WebDriverWait(self._driver, 10).until(ec.url_changes(url))

    def get_actual_product_num(self):
        wait(self.actual_products_num_info.is_displayed)
        actual_product_num = self.actual_products_num_info.text.split(sep=" ")[4]
        return actual_product_num
