import logging
import allure
from pages.base_page_object import BasePageObject
from webium import BasePage
from pages.new_address_page import NewAddressPage

LOGGER = logging.getLogger(__name__)


class NewAddressActions(BasePage, BasePageObject):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.new_address_actions = NewAddressPage(driver=self.driver)

    @allure.step("Open new address form")
    def open_new_address_form(self):
        LOGGER.info("Open new address form")
        self.new_address_actions.click_change_shipping_address_button()
        self.new_address_actions.click_add_new_address_button()

    @allure.step("Fill in new address info")
    def fill_in_new_address(self, nickname, company_name, phone_number, address, city, zip_code, county):
        LOGGER.info("Fill in new address info")
        self.new_address_actions.type_new_address_nickname(value=nickname)
        self.new_address_actions.type_new_address_company_name(value=company_name)
        self.new_address_actions.type_new_address_phone_number(value=phone_number)
        self.new_address_actions.type_new_address(value=address)
        self.new_address_actions.type_new_address_city(value=city)
        self.new_address_actions.type_new_address_zip_code(value=zip_code)
        self.new_address_actions.type_new_address_county(value=county)
        self.new_address_actions.click_ship_to_new_address_option()
        self.new_address_actions.click_bill_to_new_address_option()

    @allure.step("Save new address")
    def save_new_address(self):
        LOGGER.info("Save new address")
        self.new_address_actions.click_save_new_address_button()