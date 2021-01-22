from seleniumwire import webdriver
from pathlib import Path
from selenium.common.exceptions import WebDriverException
import webium.settings
import logging
import base64
from actions.home_page import HomePageActions
from actions.login import LoginActions
from actions.shop import ShopActions
from actions.order import OrderActions
from actions.review import ReviewActions
from actions.new_address import NewAddressActions

LOGGER_SELENIUM = logging.getLogger('seleniumwire')
LOGGER_SELENIUM.setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self, browser, base_url, config):
        # Set browser
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-application-cache")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            chrome_options.add_argument('--window-size=1920,1080')
            # chrome_options.add_argument("--log-level=3")
            driver_folder = Path("../data")
            file_to_open = driver_folder / "chromedriver.exe"
            self.driver = webdriver.Chrome(options=chrome_options,
                                           executable_path=file_to_open)
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Sets a sticky timeout to implicitly wait for an element to be found
        self.driver.implicitly_wait(3)
        webium.settings.wait_timeout = 5
        # Invokes the window manager-specific 'full screen' operation
        LOGGER.info("Expand browser to full screen")
        self.driver.maximize_window()
        # Delete all cookies in the scope of the session
        self.driver.delete_all_cookies()
        # Initialize pages
        LOGGER.info("Started browser")
        self.home_page_actions = HomePageActions(self)
        self.login_actions = LoginActions(self)
        self.shop_actions = ShopActions(self)
        self.order_actions = OrderActions(self)
        self.review_actions = ReviewActions(self)
        self.new_address_actions = NewAddressActions(self)
        self.driver.request_interceptor = self.interceptor
        self.base_url = base_url
        self.config = config

    def navigate_to_home_page(self):
        driver = self.driver
        driver.get(self.base_url)
        LOGGER.info("Open url '%s'", self.base_url)

    def authorize(self):
        self.home_page_actions.open_login_frame()
        self.login_actions.type_credentials(
            email=self.config["login"]["email"],
            password=self.config["login"]["password"]
        )
        self.login_actions.submit_credentials()

    def destroy(self):
        # Stop the browser
        self.driver.quit()
        LOGGER.info("Quits the driver and closes every associated window.")

    # Verify the URL of the current page.
    def is_valid(self):
        try:
            self.current_url()
            LOGGER.info("Browser is valid")
            return True
        except WebDriverException:
            return False

    # Gets the URL of the current page.
    def current_url(self):
        return self.driver.current_url

    def interceptor(self, request):
        username = self.config["basic_auth"]["username"]
        password = self.config["basic_auth"]["password"]
        encode = base64.b64encode(f"{username}:{password}".encode('ascii'))
        request.headers['Authorization'] = "Basic YWRtaW46dGlnaUAyMDIxIQ=="
