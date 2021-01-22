import logging

from webium import BasePage
from pages.base_page_object import BasePageObject
from pages.order_page import OrderPage
import allure

LOGGER = logging.getLogger(__name__)


class OrderActions(BasePage, BasePageObject):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.order_actions = OrderPage(driver=self.driver)

    @allure.step("Choose payment method option")
    def select_payment_method_option(self, option_text):
        LOGGER.info("Choose payment method option")
        self.order_actions.click_payment_method_button()
        self.order_actions.choose_payment_method_option(
            option_text=option_text
        )

    @allure.step("Fill in specified PO number")
    def fill_in_po_number(self, po_number):
        LOGGER.info("Fill in specified PO number")
        self.order_actions.type_po_number(
            value=po_number
        )
        self.order_actions.click_submit_po_button()

    @allure.step("Set checkout options")
    def set_checkout_options(self):
        LOGGER.info("Set checkout options")
        self.order_actions.click_change_shipping_address_button()
        self.order_actions.click_address_option()
        self.order_actions.click_change_billing_address_button()
        self.order_actions.click_address_option()

    @allure.step("Accept order info")
    def accept_order_info(self):
        LOGGER.info("Accept order info")
        self.order_actions.click_place_order_button()

    @allure.step("Verify order confirmation")
    def verify_order_confirmation(self, url):
        LOGGER.info("Verify order confirmation")
        assert url in self.driver.current_url, f"Test create order failed." \
                                               f"Expected url: {url}, " \
                                               f"Actual url: {self.driver.current_url}"
