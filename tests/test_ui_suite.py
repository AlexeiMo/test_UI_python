import pytest
from time import sleep


@pytest.mark.ui
class TestUISuite(object):

    @pytest.fixture(scope="function")
    @pytest.mark.tcid0
    def test_navigate_home_page(self, app):
        app.navigate_to_home_page()
        app.home_page_actions.verify_url(
            url=app.config["web"]["baseUrl"]
        )
        app.home_pageions.verify_page_content()

    @pytest.mark.auth
    @pytest.mark.tcid1
    def test_login(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.login_actions.type_credentials(
            email=app.config["login"]["email"],
            password=app.config["login"]["password"]
        )
        app.login_actions.submit_credentials()
        app.home_page_actions.verify_login()

    @pytest.mark.auth
    @pytest.mark.tcid5
    def test_invalid_login(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.logout()
        app.home_page_actions.open_login_frame()
        app.login_actions.type_credentials(
            email=app.config["login"]["wrong_email"],
            password=app.config["login"]["wrong_password"]
        )
        app.login_actions.submit_credentials()

    @pytest.mark.auth
    @pytest.mark.tcid8
    def test_logout(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.open_login_frame()
        app.login_actions.type_credentials(
            email=app.config["login"]["email"],
            password=app.config["login"]["password"]
        )
        app.login_actions.submit_credentials()
        app.home_page_actions.logout()
        app.home_page_actions.verify_logout()

    @pytest.mark.tcid6
    def test_default_sort_option(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        app.shop_actions.verify_sort_option(
            option_name=app.config["shop"]["default_option"]
        )

    @pytest.mark.tcid12
    def test_search(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.search_item(
            option=app.config["search"]["option"]
        )
        app.shop_actions.verify_search_results_info()

    @pytest.mark.test
    @pytest.mark.tcid2
    def test_order(self, app):
        app.navigate_to_home_page()
        sleep(3)
        app.authorize()
        sleep(3)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        sleep(3)
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        sleep(3)
        app.shop_actions.add_product_to_cart(index=0)
        app.shop_actions.add_product_to_cart(index=1)
        app.shop_actions.open_order_menu()
        # sleep(5)
        app.order_actions.select_payment_method_option(
            option_text=app.config["order"]["option"]
        )
        app.order_actions.fill_in_po_number(
            po_number=app.config["order"]["invoice_number"]
        )
        app.order_actions.set_checkout_options()
        # sleep(2)
        app.order_actions.accept_order_info()
        # sleep(5)
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )
