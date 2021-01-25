from selenium.webdriver.common.by import By
from webium.wait import wait
from webium import BasePage, Find, Finds


class OrderSummaryPage(BasePage):
    open_rec_frame_button = Find(
        by=By.XPATH,
        value="//button[.='Make a recurring order']"
    )
    recurring_order_frame = Find(
        by=By.XPATH,
        value="//h2[.='Create a recurring order']/../../.."
    )
    name_field = Find(
        by=By.ID,
        value="CC-checkoutScheduledOrder-sname"
    )
    start_date_field = Find(
        by=By.ID,
        value="CC-checkoutScheduledOrder-sstartdate"
    )
    end_date_field = Find(
        by=By.ID,
        value="CC-checkoutScheduledOrder-senddatetype"
    )
    schedule_mode_field = Find(
        by=By.ID,
        value="CC-scheduledOrder-scheduleMode"
    )
    close_rec_frame_button = Find(
        by=By.XPATH,
        value="//h2[.='Create a recurring order']/../button"
    )
    line_items_number_icon = Find(
        by=By.CSS_SELECTOR,
        value="span[class='cart-summary__total-items-text']"
    )
    total_items_number_icon = Find(
        by=By.CSS_SELECTOR,
        value="span[class='cart-summary__total-qty-text']"
    )
    salon_total_icon = Find(
        by=By.XPATH,
        value="//span[.='Salon Price']/.."
    )
    your_total_icon = Find(
        by=By.XPATH,
        value="//span[.='Your Price']/.."
    )
    sales_tax_icon = Find(
        by=By.XPATH,
        value="//span[.='Sales Tax: ']/.."
    )
    shipping_icon = Find(
        by=By.XPATH,
        value="//span[.='Shipping: ']/.."
    )

    def click_open_rec_frame(self):
        wait(self.open_rec_frame_button.is_displayed)
        self.open_rec_frame_button.click()

    def click_close_rec_frame(self):
        wait(self.close_rec_frame_button.is_displayed)
        self.close_rec_frame_button.click()

    def is_recurring_order_displayed(self):
        wait(self.recurring_order_frame.is_displayed)
        return self.recurring_order_frame.is_displayed()
