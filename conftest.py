import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/home/burn/chromedriver")
    yield driver
    driver.quit()
