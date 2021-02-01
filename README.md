# Webdriver Testing

Selenium testing using Webium framework for "https://ccstore-test-zd3a.oracleoutsourcing.com"


## Key Features
- Tests are written in Python (pytest)
- Tests can be run on Google Chrome browser (Chrome driver used)
- Tests running can create allure results to build allure reports then

## Repo Layout

- test_UI_python/actions - test's actions for specified pages.
- test_UI_python/data - stored webdrivers which is used to interface specified browsers.
- test_UI_python/pages - Page objects used to manipulate with test pages
- test_UI_python/tests - tests which can be run on pytest
- test_UI_python/utilities - different utilities used in tests
  (e.g. generating random string for credentials)

## Config
- test_UI_python/fixture/application.py - main application
  object used to configure test environment (e.g. browser options)
- test_UI_python/pytest.ini - configuration file for pytest
- test_UI_python/target.json - data used in tests (e.g. user credentials,
  base url for browser)
- test_UI_python/conftest.py - configuration file that links
  main application with target.json
- test_UI_python/requirements.txt - file used in
  Python environment configuration


## Usage

### Install/Build
Run commands in terminal IDE:
1. Install python3
2. python3 -m venv env (create env)
3. cd env\\Scripts (go to env activation folder)
4. activate.bat (activate env)
5. pip install -r requirements.txt (install dependencies from requirements.txt file)


### Run Project Tests (Locally)
Run commands in terminal IDE:
1. cd test (go to test folder into the project)
2. pytest --alluredir=allure-results (run api tests)
3. allure generate allure-results --clean -o allure-report (generate allure report)

### Run Project Tests (Docker Container)
Run commands in terminal IDE:
1. docker build -t ui . (build docker image)
2. docker run --rm --name ui_test ui (run docker container)

OR

Run commands in terminal IDE:
1. docker-compose up (creating image and running container)
2. allure generate allure-results --clean -o allure-report (generate allure report)

#### target.json
Requires valid username/password configured in target.json for
Basic authentication and valid email/password for valid login
process (required quite for all tests)
```json
{
    "basic_auth": {
        "username": "<browserstack-username>",
        "password": "<browserstack-password>"
    },
    "login": {
      "email": "<login-email>",
      "password": "<login-password>"
    }
}
```

## Notes
- Seleniumwire package is used in project to pass Basic
  Authentication (see test_UI_python/fixtures/application.py)