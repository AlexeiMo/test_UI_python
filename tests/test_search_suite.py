import pytest

from conftest import capture_screenshot


@pytest.mark.search
class TestSearchSuite:

    @capture_screenshot
    @pytest.mark.tcid50
    def test_search_one_item(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.wait_for_home_page_loaded()
        app.home_page_actions.search_item(
            option=app.config["search_one_item"]["option"]
        )
        app.shop_actions.verify_search_one_item(
            url=app.config["search_one_item"]["url"]
        )
