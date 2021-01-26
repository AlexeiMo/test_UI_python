import pytest
from time import sleep


@pytest.mark.userflow
class TestUserflowSuite:

    @pytest.mark.tcid2
    def test_checkout_with_po_number(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        app.shop_actions.wait_for_plp_loaded()
        app.shop_actions.add_product_to_cart(index=1)
        app.shop_actions.open_order_menu()
        app.order_actions.wait_for_pdp_loaded()
        app.order_actions.select_payment_method_option(
            option_text=app.config["po_checkout"]["option"]
        )
        app.order_actions.fill_in_po_number(
            po_number=app.config["po_checkout"]["invoice_number"]
        )
        app.order_actions.set_checkout_options()
        app.order_actions.accept_order_info()
        app.order_actions.wait_for_order_confirmation()
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )

    @pytest.mark.tcid3
    def test_checkout_with_visa_card(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        app.shop_actions.wait_for_plp_loaded()
        app.shop_actions.add_product_to_cart(index=1)
        app.shop_actions.open_order_menu()
        app.order_actions.wait_for_pdp_loaded()
        app.order_actions.select_payment_method_option(
            option_text=app.config["visa_checkout"]["option"]
        )
        app.order_actions.set_checkout_options()
        app.order_actions.accept_order_info()
        app.order_actions.wait_for_order_confirmation()
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )

    @pytest.mark.tcid4
    def test_checkout_with_new_shipping_address(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        app.shop_actions.wait_for_plp_loaded()
        app.shop_actions.add_product_to_cart(index=1)
        app.shop_actions.open_order_menu()
        app.order_actions.wait_for_pdp_loaded()
        app.order_actions.select_payment_method_option(
            option_text=app.config["visa_checkout"]["option"]
        )
        app.new_address_actions.open_new_address_form()
        app.new_address_actions.fill_in_new_address(
            company_name=app.config["new_address"]["company_name"],
            phone_number=app.config["new_address"]["phone_number"],
            address=app.config["new_address"]["address"],
            city=app.config["new_address"]["city"],
            state=app.config["new_address"]["state"],
            zip_code=app.config["new_address"]["zip_code"],
            county=app.config["new_address"]["county"],
            country=app.config["new_address"]["country"]
        )
        app.new_address_actions.save_new_address()
        app.order_actions.accept_order_info()
        app.order_actions.wait_for_order_confirmation()
        app.order_actions.verify_order_confirmation(
            url=app.config["order"]["confirmation_page_url"]
        )
