import pytest

from conftest import capture_screenshot


@pytest.mark.order
class TestOrderSuite:

    @capture_screenshot
    @pytest.mark.tcid360
    def test_verify_order_summary(self, app):
        app.navigate_to_home_page()
        app.home_page_actions.verify_url(
            url=app.config["web"]["baseUrl"]
        )
        app.authorize()
        app.home_page_actions.wait_for_home_page_loaded()
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
        # app.order_actions.set_checkout_options()
        app.order_actions.wait_for_pdp_loaded()
        app.order_summary_actions.verify_order_summary()
