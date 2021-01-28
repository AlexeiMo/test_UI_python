from webium.wait import wait
from webium import BasePage, Find, Finds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class NewAddressPage(BasePage):
    change_shipping_address_button = Find(
        by=By.XPATH,
        value="//button[.='Change Shipping Address']"
    )
    add_new_address_button = Find(
        by=By.XPATH,
        value="//button[.='Add a New Address']"
    )
    new_address_nickname_field = Find(
        by=By.ID,
        value="nicknameNew"
    )
    new_address_company_name_field = Find(
        by=By.ID,
        value="companyNameNew"
    )
    new_address_phone_number_field = Find(
        by=By.ID,
        value="phoneNew"
    )
    new_address_field = Find(
        by=By.ID,
        value="address1New"
    )
    new_address_city_field = Find(
        by=By.ID,
        value="cityNew"
    )
    new_address_state_field = Find(
        by=By.ID,
        value="stateNew"
    )
    new_address_zip_code_field = Find(
        by=By.ID,
        value="zipNew"
    )
    new_address_county_field = Find(
        by=By.ID,
        value="countyNew"
    )
    new_address_country_field = Find(
        by=By.ID,
        value="countryNew"
    )
    bill_to_new_address_option = Find(
        by=By.XPATH,
        value="//input[@id='billToThisAddress']/../label/div"
    )
    ship_to_new_address_option = Find(
        by=By.XPATH,
        value="//input[@id='shipToThisAddress']/../label/div"
    )
    save_new_address_button = Find(
        by=By.XPATH,
        value="//div[@class='col-xs-12 mb-4 mt-3']/button[.='Save']"
    )

    def click_change_shipping_address_button(self):
        wait(self.change_shipping_address_button.is_displayed)
        self.change_shipping_address_button.click()

    def click_add_new_address_button(self):
        wait(self.add_new_address_button.is_displayed)
        self.add_new_address_button.click()

    def type_new_address_nickname(self, value):
        wait(self.new_address_nickname_field.is_displayed)
        self.new_address_nickname_field.send_keys(value)

    def type_new_address_company_name(self, value):
        wait(self.new_address_company_name_field.is_displayed)
        self.new_address_company_name_field.send_keys(value)

    def type_new_address_phone_number(self, value):
        wait(self.new_address_phone_number_field.is_displayed)
        self.new_address_phone_number_field.send_keys(value)

    def type_new_address(self, value):
        wait(self.new_address_field.is_displayed)
        self.new_address_field.send_keys(value)

    def type_new_address_city(self, value):
        wait(self.new_address_city_field.is_displayed)
        self.new_address_city_field.send_keys(value)

    def type_new_address_state(self, value):
        wait(self.new_address_state_field.is_displayed)
        self.new_address_state_field.send_keys(value)

    def type_new_address_zip_code(self, value):
        wait(self.new_address_zip_code_field.is_displayed)
        self.new_address_zip_code_field.send_keys(value)

    def type_new_address_county(self, value):
        wait(self.new_address_county_field.is_displayed)
        self.new_address_county_field.send_keys(value)

    def type_new_address_country(self, value):
        wait(self.new_address_country_field.is_displayed)
        self.new_address_country_field.send_keys(value)

    def click_ship_to_new_address_option(self):
        wait(self.ship_to_new_address_option.is_displayed)
        self.ship_to_new_address_option.click()

    def click_bill_to_new_address_option(self):
        wait(self.bill_to_new_address_option.is_displayed)
        self.bill_to_new_address_option.click()

    def click_save_new_address_button(self):
        wait(self.save_new_address_button.is_displayed)
        self.save_new_address_button.click()
