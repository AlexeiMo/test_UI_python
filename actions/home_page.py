import logging

from webium import BasePage
from pages.base_page_object import BasePageObject
from pages.home_page import HomePage
import allure
from allure import attachment_type

LOGGER = logging.getLogger(__name__)


class HomePageActions(BasePage, BasePageObject):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.home_page_actions = HomePage(driver=self.driver)

    @allure.step("Verify navigating to home page")
    def verify_url(self, url):
        LOGGER.info("Verify navigating to home page")
        assert self.driver.current_url == url, f"Test navigate to home page failed. " \
                                               f"Expected url: {url}, " \
                                               f"Actual url: {self.driver.current_url}"
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)

    @allure.step("Verify content of home page")
    def verify_page_content(self):
        LOGGER.info("Verify content of home page")
        assert self.home_page_actions.login_frame.is_displayed(), "Test navigate to home page failed. " \
                                                                  "Login frame is not displayed."

    @allure.step("Verify login process")
    def verify_login(self):
        LOGGER.info("Verify login process")
        assert self.home_page_actions.account_icon.is_displayed(), "Login failed."
        assert self.home_page_actions.welcome_text.is_displayed(), "Login failed."
        assert self.home_page_actions.cart_icon.is_displayed(), "Login failed."
        self.app.is_logged = True
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)

    @allure.step("Logout user from site")
    def logout(self):
        LOGGER.info("Logout user from site")
        self.home_page_actions.click_account_settings()
        self.home_page_actions.click_logout_link()
        self.app.is_logged = False

    @allure.step("Verify invalid login process")
    def verify_invalid_login(self):
        LOGGER.info("Verify invalid login process")
        assert self.home_page_actions.is_invalid_login_message_displayed(), "Test invalid login failed. " \
                                                                            "No invalid login message was shown"
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)

    @allure.step("Navigate to specified category")
    def navigate_to_category(self, name):
        LOGGER.info("Navigate to specified category")
        self.home_page_actions.click_category_link(name)
        
    @allure.step("Navigate to specified subcategory")
    def navigate_to_subcategory(self, name):
        LOGGER.info("Navigate to specified subcategory")
        self.home_page_actions.click_subcategory_link(name)

    @allure.step("Search specified option")
    def search_item(self, option):
        LOGGER.info("Search specified option")
        self.home_page_actions.type_search_option(option=option)
        self.home_page_actions.click_search_button()

    @allure.step("Open login frame")
    def open_login_frame(self):
        LOGGER.info("Open login frame")
        if not self.home_page_actions.login_frame.is_displayed():
            self.home_page_actions.click_login_button()

    @allure.step("Verify logout process")
    def verify_logout(self):
        LOGGER.info("Verify logout process")
        assert self.home_page_actions.login_button.is_displayed(), "Test logout failed. " \
                                                                   "Login button is missed."
        # assert self.home_page_actions.country_selector.is_displayed(), "Test logout failed." \
        #                                                                "Country selector is missed."
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)

    @allure.step("Wait for home page loaded")
    def wait_for_home_page_loaded(self):
        LOGGER.info("Wait for home page loaded")
        self.home_page_actions.wait_for_home_page_loaded()
