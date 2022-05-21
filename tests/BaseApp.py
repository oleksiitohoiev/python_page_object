from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://djinni.co/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_title(self, title, time=10):
        return WebDriverWait(self.driver, time).until(ec.title_contains(title), message=f"Can't find title {title}")

    def is_element_clickable(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))
        except NoSuchElementException as e:
            return e
        return True




