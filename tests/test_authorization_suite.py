import pytest
from time import sleep


@pytest.mark.auth
class TestAuthorizationSuite:

    @pytest.mark.tcid1
    def test_login(self, app):
        app.navigate_to_home_page()
        app.home_page_actions.open_login_frame()
        app.login_actions.type_credentials(
            email=app.config["login"]["email"],
            password=app.config["login"]["password"]
        )
        app.login_actions.submit_credentials()
        app.home_page_actions.verify_login()

    @pytest.mark.tcid5
    def test_invalid_login(self, app):
        app.navigate_to_home_page()
        app.authorize()
        sleep(5)
        app.home_page_actions.logout()
        app.home_page_actions.open_login_frame()
        app.login_actions.type_credentials(
            email=app.config["login"]["wrong_email"],
            password=app.config["login"]["wrong_password"]
        )
        app.login_actions.submit_credentials()
        app.home_page_actions.verify_invalid_login()

    @pytest.mark.tcid8
    def test_logout(self, app):
        app.navigate_to_home_page()
        app.authorize()
        sleep(5)
        app.home_page_actions.logout()
        app.home_page_actions.verify_logout()
