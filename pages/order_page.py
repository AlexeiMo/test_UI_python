from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support.select import Select


class OrderPage(BasePage):
    payment_method_button = Find(
        by=By.XPATH,
        value="//span[.='Select New Payment Method']/.."
    )
    payment_method_options = Finds(
        by=By.CSS_SELECTOR,
        value="li[class='g-fancy-dropdown__item']"
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

    def click_payment_method_button(self):
        wait(self.payment_method_button.is_displayed)
        self.payment_method_button.click()

    def choose_payment_method_option(self, option_text):
        for option in self.payment_method_options:
            wait(option.is_displayed)
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
        wait(self.change_shipping_address_button.is_displayed)
        self.change_shipping_address_button.click()

    def click_address_option(self):
        wait(self.address_option.is_displayed)
        self.address_option.click()

    def click_change_billing_address_button(self):
        wait(self.change_billing_address_button.is_displayed)
        self.change_billing_address_button.click()

    def click_place_order_button(self):
        wait(self.place_order_button.is_displayed)
        self.place_order_button.click()
