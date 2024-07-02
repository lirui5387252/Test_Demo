import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.taobao.home_page import HomePage
from pages.taobao.login_page import LoginPage


@pytest.fixture(scope="module")
def setup():
    # Setup WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Teardown WebDriver
    driver.quit()


def test_search_product(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.open_url("https://www.taobao.com/")
    home_page.search_for_product("laptop")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.item'))
    )
    assert "laptop" in driver.title


def test_login(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.open_url("https://www.taobao.com/")
    home_page.go_to_login_page()

    login_page = LoginPage(driver)
    login_page.enter_username("your_username")
    login_page.enter_password("your_password")
    login_page.click_login_button()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.user-nick'))
    )

    assert "Taobao" in driver.title
