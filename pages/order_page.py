from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OrderPage(BasePage):
    payment_method_button = Find(
        by=By.XPATH,
        value="//span[.='Select New Payment Method']/.."
    )
    payment_method_options = Finds(
        by=By.CSS_SELECTOR,
        value="li[class='g-fancy-dropdown__item']"
    )
    payment_method_frame = Find(
        by=By.CSS_SELECTOR,
        value="ul[data-bind='foreach: options']"
    )
    po_number_input = Find(by=By.ID, value="poNumber")
    submit_po_number_button = Find(
        by=By.XPATH,
        value="//button[.='Submit']"
    )
    change_shipping_address_button = Find(
        by=By.XPATH,
        value="//button[.='Change Shipping Address']"
    )
    address_option = Find(
        by=By.XPATH,
        value="//input[@id='address-0']/../label/div"
    )
    change_billing_address_button = Find(
        by=By.XPATH,
        value="//button[.='Change Billing Address']"
    )
    place_order_button = Find(
        by=By.XPATH,
        value="//span[.='Place Order']/.."
    )

    print_confirmation_button = Find(
        by=By.XPATH,
        value="//button[.='Print Confirmation']"
    )

    support_button = Find(
        by=By.XPATH,
        value="//span[.='Contact Customer Support']"
    )
    price_before = ""
    price = Find(
        by=By.XPATH,
        value="//g-price[@params='price: cart().total()']/span"
    )

    def click_payment_method_button(self):
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Select New Payment Method']/..")
        ))
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@class='col-xs-12 col-sm-6 mt-3 mb-3']/img")
        ))
        self._driver.find_element_by_xpath("//span[.='Select New Payment Method']/..").click()

    def choose_payment_method_option(self, option_text):
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul[data-bind='foreach: options']")
        ))
        WebDriverWait(self._driver, 15).until(ec.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "li[class='g-fancy-dropdown__item']")
        ))
        for option in self.payment_method_options:
            WebDriverWait(self._driver, 15).until(ec.visibility_of(option))
            if option.text == option_text:
                option.click()
                break
        else:
            raise Exception("No such option was found")

    def type_po_number(self, value):
        wait(self.po_number_input.is_displayed)
        self.po_number_input.send_keys(value)

    def click_submit_po_button(self):
        wait(self.submit_po_number_button.is_displayed)
        self.submit_po_number_button.click()

    def click_change_shipping_address_button(self):
        # wait(self.change_shipping_address_button.is_displayed)
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//button[.='Change Shipping Address']")
        ))
        self.change_shipping_address_button.click()

    def click_address_option(self):
        wait(self.address_option.is_displayed)
        self.address_option.click()

    def click_change_billing_address_button(self):
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//button[.='Change Billing Address']")
        ))
        self.change_billing_address_button.click()

    def click_place_order_button(self):
        wait(self.place_order_button.is_displayed)

        self.place_order_button.click()

    def wait_for_pdp_loaded(self):
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Contact Customer Support']")
        ))
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Place Order']/..")
        ))
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//button[.='Change Billing Address']")
        ))
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Select New Payment Method']/..")
        ))
        wait(lambda: self.price.text != self.price_before)
        self.price_before = self.price.text

    def wait_for_order_confirmation(self):
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Contact Customer Support']")
        ))
        WebDriverWait(self._driver, 15).until(ec.url_contains(
            url="https://ccstore-test-zd3a.oracleoutsourcing.com/us/confirmation/"
        ))
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.XPATH, "//h2[.='You Might Also Like']/..")
        ))
