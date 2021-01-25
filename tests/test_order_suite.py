import pytest
from time import sleep


@pytest.mark.order
class TestOrderSuite:

    @pytest.mark.tcid360
    def test_verify_order_summary(self, app):
        app.navigate_to_home_page()
        app.home_page_actions.verify_url(
            url=app.config["web"]["baseUrl"]
        )
        app.authorize()
        app.home_page_actions.navigate_to_category(
            name=app.config["home_page"]["category_name"]
        )
        sleep(4)
        app.home_page_actions.navigate_to_subcategory(
            name=app.config["home_page"]["subcategory_name"]
        )
        sleep(5)
        app.shop_actions.add_product_to_cart(index=0)
        app.shop_actions.add_product_to_cart(index=1)
        app.shop_actions.open_order_menu()
        sleep(5)
        app.order_actions.select_payment_method_option(
            option_text=app.config["visa_checkout"]["option"]
        )
        app.order_actions.set_checkout_options()
        app.order_summary_actions.verify_order_summary()
