import pytest
from time import sleep


# PLP - Product Listing Page
@pytest.mark.plp
class TestPLPSuite:

    @pytest.mark.tcid6
    def test_default_sort_option(self, app):
        app.navigate_to_home_page()
        app.authorize()
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
        app.authorize()
        app.home_page_actions.search_item(
            option=app.config["search"]["option"]
        )
        app.shop_actions.verify_search_results_info()
