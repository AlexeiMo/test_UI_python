import pytest
from time import sleep


@pytest.mark.ui
class TestUISuite(object):

    @pytest.mark.tcid0
    def test_navigate_home_page(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.verify_url(
            url=app.config["web"]["baseUrl"]
        )
        app.home_page_actions.verify_page_content()

    @pytest.mark.auth
    @pytest.mark.tcid1
    def test_login(self, app):
        app.navigate_to_home_page()
        sleep(7)
        app.home_page_actions.open_login_frame()
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
        app.home_page_actions.verify_invalid_login()

    @pytest.mark.auth
    @pytest.mark.tcid8
    def test_logout(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.open_login_frame()
        app.login_actions.type_credentials(
            email=app.config["login"]["email"],
            password=app.config["login"]["password"]
        )
        app.login_actions.submit_credentials()
        app.home_page_actions.logout()
        app.home_page_actions.verify_logout()

    @pytest.mark.userflow
    @pytest.mark.tcid2
    def test_checkout_with_po_number(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.authorize()
        sleep(5)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        sleep(5)
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        sleep(5)
        app.shop_actions.add_product_to_cart(index=0)
        sleep(1)
        app.shop_actions.add_product_to_cart(index=1)
        sleep(1)
        app.shop_actions.open_order_menu()
        sleep(5)
        app.order_actions.select_payment_method_option(
            option_text=app.config["po_checkout"]["option"]
        )
        app.order_actions.fill_in_po_number(
            po_number=app.config["po_checkout"]["invoice_number"]
        )
        app.order_actions.set_checkout_options()
        sleep(7)
        app.order_actions.accept_order_info()
        sleep(5)
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )

    @pytest.mark.userflow
    @pytest.mark.tcid3
    def test_checkout_with_visa_card(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        sleep(5)
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        sleep(5)
        app.shop_actions.add_product_to_cart(index=0)
        sleep(1)
        app.shop_actions.add_product_to_cart(index=1)
        sleep(1)
        app.shop_actions.open_order_menu()
        sleep(5)
        app.order_actions.select_payment_method_option(
            option_text=app.config["visa_checkout"]["option"]
        )
        app.order_actions.set_checkout_options()
        sleep(7)
        app.order_actions.accept_order_info()
        sleep(5)
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )

    @pytest.mark.userflow
    @pytest.mark.tcid4
    def test_checkout_with_new_shipping_address(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.authorize()
        sleep(5)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        sleep(5)
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        sleep(5)
        app.shop_actions.add_product_to_cart(index=0)
        sleep(1)
        app.shop_actions.add_product_to_cart(index=1)
        sleep(1)
        app.shop_actions.open_order_menu()
        sleep(5)
        app.order_actions.select_payment_method_option(
            option_text=app.config["visa_checkout"]["option"]
        )
        app.new_address_actions.open_new_address_form()
        app.new_address_actions.fill_in_new_address(
            nickname=app.config["new_address"]["nickname"],
            company_name=app.config["new_address"]["company_name"],
            phone_number=app.config["new_address"]["phone_number"],
            address=app.config["new_address"]["address"],
            city=app.config["new_address"]["city"],
            zip_code=app.config["new_address"]["zip_code"],
            county=app.config["new_address"]["county"]
        )
        app.new_address_actions.save_new_address()

    @pytest.mark.plp
    @pytest.mark.tcid6
    def test_default_sort_option(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        app.shop_actions.verify_sort_option(
            option_name=app.config["shop"]["default_option"]
        )

    @pytest.mark.plp
    @pytest.mark.tcid12
    def test_search(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.search_item(
            option=app.config["search"]["option"]
        )
        sleep(5)
        app.shop_actions.verify_search_results_info()

    @pytest.mark.pdp
    @pytest.mark.tcid36
    def test_create_review(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.search_item(
            option=app.config["review"]["option"]
        )
        sleep(7)
        app.review_actions.open_review_form()
        app.review_actions.fill_in_review(
            title=app.config["review"]["title"],
            content=app.config["review"]["content"],
            username=app.config["review"]["username"],
            email=app.config["review"]["email"]
        )
        app.review_actions.post_review()
        app.review_actions.verify_review(
            title=app.config["review"]["title"],
            content=app.config["review"]["content"]
        )

    @pytest.mark.search
    @pytest.mark.tcid50
    def test_search_one_item(self, app):
        app.navigate_to_home_page()
        sleep(5)
        app.home_page_actions.search_item(
            option=app.config["search_one_item"]["option"]
        )
        sleep(7)
        app.shop_actions.verify_search_one_item(
            url=app.config["search_one_item"]["url"]
        )
