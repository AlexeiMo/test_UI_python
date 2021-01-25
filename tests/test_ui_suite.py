import pytest


@pytest.mark.ui
class TestUISuite(object):

    @pytest.mark.tcid0
    def test_navigate_home_page(self, app):
        app.navigate_to_home_page()
        app.home_page_actions.verify_url(
            url=app.config["web"]["baseUrl"]
        )
