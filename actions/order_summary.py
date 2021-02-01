import logging
import allure
from pages.base_page_object import BasePageObject
from pages.order_summary_page import OrderSummaryPage
from webium import BasePage
from webium.wait import wait
from allure import attachment_type

LOGGER = logging.getLogger(__name__)


class OrderSummaryActions(BasePage, BasePageObject):

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.order_summary_actions = OrderSummaryPage(driver=self.driver)

    @allure.step("Verify recurring order frame")
    def verify_recurring_order_frame(self):
        LOGGER.info("Verify recurring order frame")
        self.order_summary_actions.click_open_rec_frame()
        wait(self.order_summary_actions.recurring_order_frame.is_displayed)
        assert self.order_summary_actions.name_field.is_displayed(), "Test verify order summary failed. " \
                                                                     "No name field was shown"
        assert self.order_summary_actions.start_date_field.is_displayed(), "Test verify order summary failed. " \
                                                                           "No start date field was shown"
        assert self.order_summary_actions.end_date_field.is_displayed(), "Test verify order summary failed. " \
                                                                         "No end date field was shown"
        assert self.order_summary_actions.schedule_mode_field.is_displayed(), "Test verify order summary failed. " \
                                                                              "No schedule mode field was shown"
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)
        self.order_summary_actions.click_close_rec_frame()
        self.driver.switch_to.parent_frame()

    @allure.step("Verify order summary content")
    def verify_order_summary(self):
        LOGGER.info("Verify order summary content")
        self.verify_recurring_order_frame()
        assert self.order_summary_actions.salon_total_icon.is_displayed(), "Test verify order summary failed. " \
                                                                          "No salon total icon was shown"
        assert self.order_summary_actions.your_total_icon.is_displayed(), "Test verify order summary failed. " \
                                                                          "No your total icon was shown"
        assert self.order_summary_actions.sales_tax_icon.is_displayed(), "Test verify order summary failed. " \
                                                                         "No sales tax icon was shown"
        assert self.order_summary_actions.shipping_icon.is_displayed(), "Test verify order summary failed. " \
                                                                        "No shipping icon was shown"
        allure.attach(self.driver.get_screenshot_as_png(), "screenshot", attachment_type.PNG)
