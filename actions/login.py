import logging

from webium import BasePage
from pages.base_page_object import BasePageObject
from pages.login_page import LoginPage
import allure

LOGGER = logging.getLogger(__name__)


class LoginActions(BasePage, BasePageObject):
    
    # Get an instance driver, app, page locators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPage(driver=self.driver)

    @allure.step("Type credentials")
    def type_credentials(self, email, password):
        LOGGER.info("Type credentials")
        self.login_actions.type_email(email)
        self.login_actions.type_password(password)
    
    @allure.step("Submit credentials")
    def submit_credentials(self):
        LOGGER.info("Submit credentials")
        self.login_actions.click_submit_button()
