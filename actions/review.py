import allure
import logging
from pages.base_page_object import BasePageObject
from pages.review_page import ReviewPage
from webium import BasePage

LOGGER = logging.getLogger(__name__)


class ReviewActions(BasePage, BasePageObject):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.review_actions = ReviewPage(driver=self.driver)

    @allure.step("Open review form to write a review")
    def open_review_form(self):
        LOGGER.info("Open review form to write a review")
        self.review_actions.click_create_review_button()

    @allure.step("Fill in review info")
    def fill_in_review(self, title, content, username, email):
        LOGGER.info("Fill in review info")
        self.review_actions.click_score_option()
        self.review_actions.type_review_title(title)
        self.review_actions.type_review_content(content)
        self.review_actions.type_review_username(username)
        self.review_actions.type_review_email(email)

    @allure.step("Post review")
    def post_review(self):
        LOGGER.info("Post review")
        self.review_actions.click_post_review_button()

    @allure.step("Verify created review")
    def verify_review(self, title, content):
        LOGGER.info("Verify created review")
        review_title = self.review_actions.get_review_title()
        review_content = self.review_actions.get_review_content()
        assert review_title == title, f"Test create review failed. " \
                                      f"Expected review title: {title}, " \
                                      f"Actual review title: {review_title}"
        assert review_content == content, f"Test create review failed. " \
                                          f"Expected review content: {content}, " \
                                          f"Actual review content: {review_content}"
