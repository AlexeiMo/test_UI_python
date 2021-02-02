import pytest
from conftest import capture_screenshot

# PDP - Product Detail Page


@pytest.mark.pdp
class TestPDPSuite:

    @capture_screenshot
    @pytest.mark.tcid36
    def test_create_review(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.wait_for_home_page_loaded()
        app.home_page_actions.search_item(
            option=app.config["review"]["option"]
        )
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
