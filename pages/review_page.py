from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ReviewPage(BasePage):
    create_review_button = Find(
        by=By.XPATH,
        value="//span[.='Write A Review']/.."
    )
    score_option = Find(
        by=By.CSS_SELECTOR,
        value="span[data-score='5']"
    )
    review_title_field = Find(
        by=By.CSS_SELECTOR,
        value="input[name='review_title']"
    )
    review_content_field = Find(
        by=By.CSS_SELECTOR,
        value="textarea[name='review_content']"
    )
    review_username_field = Find(
        by=By.XPATH,
        value="//div[@class='connect-wrapper visible']/div/input[@name='display_name']"
    )
    review_email_field = Find(
        by=By.XPATH,
        value="//div[@class='connect-wrapper visible']/div/input[@name='email']"
    )
    post_review_button = Find(
        by=By.XPATH,
        value="//form[@aria-label='Write A Review Form']/div/div/div/input"
    )
    review_title = Find(
        by=By.XPATH,
        value="//div[@class='yotpo-review yotpo-regular-box']/div/div[@role='heading']"
    )
    review_content = Find(
        by=By.XPATH,
        value="//div[@class='yotpo-review yotpo-regular-box']/div/div/div[@class='content-review']"
    )

    def click_create_review_button(self):
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.XPATH, "//span[.='Write A Review']/..")
        ))
        wait(self.create_review_button.is_displayed)
        self.create_review_button.click()

    def click_score_option(self):
        wait(self.score_option.is_displayed)
        self.score_option.click()

    def type_review_title(self, value):
        wait(self.review_title_field.is_displayed)
        self.review_title_field.send_keys(value)

    def type_review_content(self, value):
        wait(self.review_content_field.is_displayed)
        self.review_content_field.send_keys(value)

    def type_review_username(self, value):
        wait(self.review_username_field.is_displayed)
        self.review_username_field.send_keys(value)

    def type_review_email(self, value):
        wait(self.review_email_field.is_displayed)
        self.review_email_field.send_keys(value)

    def click_post_review_button(self):
        wait(self.post_review_button.is_displayed)
        self.post_review_button.click()

    def get_review_title(self):
        wait(self.review_title.is_displayed)
        return self.review_title.text

    def get_review_content(self):
        wait(self.review_content.is_displayed)
        return self.review_content.text
