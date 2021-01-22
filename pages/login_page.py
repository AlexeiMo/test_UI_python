from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait


class LoginPage(BasePage):
    email_field = Find(by=By.ID, value="login-email")
    password_field = Find(by=By.ID, value="login-password")
    submit_button = Find(by=By.XPATH, value="//form/button[.='Log In']")

    def type_email(self, value):
        wait(self.email_field.is_displayed)
        self.email_field.send_keys(value)

    def type_password(self, value):
        wait(self.password_field.is_displayed)
        self.password_field.send_keys(value)

    def click_submit_button(self):
        wait(self.submit_button.is_displayed)
        self.submit_button.click()
