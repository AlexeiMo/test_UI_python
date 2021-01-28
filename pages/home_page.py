from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    login_frame = Find(by=By.ID, value="tigi-login-modal")
    log_out_link = Find(by=By.XPATH, value="//a[.='Log Out']")
    account_icon = Find(
        by=By.CSS_SELECTOR,
        value="div[id='wi2100057-account-selector-1-id']"
    )
    welcome_text = Find(
        by=By.CSS_SELECTOR,
        value="span[class='max-width-link__text']"
    )
    cart_icon = Find(
        by=By.CSS_SELECTOR,
        value="span[class='tigi-header__bag-icon__label']"
    )
    invalid_login_message = Find(
        by=By.CSS_SELECTOR,
        value="span[data-bind='text: $parent.loginMessage']"
    )
    categories_links = Finds(
        by=By.XPATH,
        value="//ul[@class='header__nav-links js-mega-menu-links']/li/a"
    )
    subcategories_links = Finds(
        by=By.XPATH,
        value="//div[@class='shop-links-list']/ul/li/a"
    )
    search_field = Find(
        by=By.ID,
        value="#sophisticated-search-wi2100057"
    )
    search_button = Find(
        by=By.CSS_SELECTOR,
        value="button[type='submit']"
    )
    login_button = Find(
        by=By.CSS_SELECTOR,
        value="button[class='btn-pure header__nav-link']"
    )
    country_selector = Find(
        by=By.XPATH,
        value="//div[@class='tigi-header__end-section__top']/g-country-selector"
    )
    support_button = Find(
        by=By.XPATH,
        value="//span[.='Contact Customer Support']"
    )
    recommends_icon = Find(
        by=By.XPATH,
        value="//h2[.='You Might Also Like']/.."
    )

    def click_category_link(self, name):
        for category in self.categories_links:
            if category.text == name:
                category.click()
                break
        else:
            raise Exception("No such category found")

    def click_subcategory_link(self, name):
        for subcategory in self.subcategories_links:
            if subcategory.text == name:
                subcategory.click()
                break
        else:
            raise Exception("No such subcategory found")

    def type_search_option(self, option):
        wait(self.search_field.is_displayed)
        self.search_field.send_keys(option)

    def click_search_button(self):
        wait(self.search_button.is_displayed)
        url = self._driver.current_url
        self.search_button.click()
        WebDriverWait(self._driver, 15).until(ec.url_changes(url))

    def click_logout_link(self):
        wait(self.log_out_link.is_displayed)
        self.log_out_link.click()

    def click_account_settings(self):
        wait(self.welcome_text.is_displayed)
        self.welcome_text.click()

    def click_login_button(self):
        wait(self.login_button.is_displayed)
        self.login_button.click()

    def is_invalid_login_message_displayed(self):
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "span[data-bind='text: $parent.loginMessage']")
        ))
        return self.invalid_login_message.is_displayed()

    def wait_for_home_page_loaded(self):
        WebDriverWait(self._driver, 15).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[.='Contact Customer Support']")
        ))
        WebDriverWait(self._driver, 15).until(ec.visibility_of_element_located(
            (By.XPATH, "//h2[.='You Might Also Like']/..")
        ))
