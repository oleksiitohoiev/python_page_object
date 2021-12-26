from BaseApp import BasePage
from selenium.webdriver.common.by import By


class DjinniHomeLocators:

    LOCATOR_SALARY_BUTTON_FOOTER = (By.XPATH, "//a[contains(text(), 'Зарплати')]")


class DjinniSearchLocators:

    LOCATOR_FILTER_AQA = (By.XPATH, "//a[contains(text(),'QA Automation')]")
    LOCATOR_FILTER_AQA_TITLE = "Статистика зарплат QA Automation на Джині"
    LOCATOR_FILTER_EXP = (By.XPATH, "//a[contains(text(),'2-5 років')]")
    LOCATOR_VACANCIES_COUNT = (By.XPATH,
               "//*[@class='summary-stastistics--item summary-stastistics--item_vacancies']//div[contains(text(), 'Всього')]/parent::div//div[@class='summary-item--value']")

    LOCATOR_CANDIDATES_COUNT = (By.XPATH,
               "//*[@class='summary-stastistics--item summary-stastistics--item_candidates']//div[contains(text(), 'Всього')]/parent::div//div[@class='summary-item--value']")


class HomeHelper(BasePage):

    def click_on_the_salary_button(self):
        self.is_element_clickable(DjinniHomeLocators.LOCATOR_SALARY_BUTTON_FOOTER, time=3)
        return self.find_element(DjinniHomeLocators.LOCATOR_SALARY_BUTTON_FOOTER, time=3).click()


class SearchHelper(BasePage):
    def click_on_the_aqa_filter(self):
        return self.find_element(DjinniSearchLocators.LOCATOR_FILTER_AQA, time=3).click()

    def check_aqa_title(self):
        return self.check_title(DjinniSearchLocators.LOCATOR_FILTER_AQA_TITLE, time=3)

    def click_exp_filter(self):
        return self.find_element(DjinniSearchLocators.LOCATOR_FILTER_EXP, time=3).click()

    def value_vacancies(self):
        data = self.find_element(DjinniSearchLocators.LOCATOR_VACANCIES_COUNT, time=3).text
        return int(data)

    def value_candidates(self):
        data = self.find_element(DjinniSearchLocators.LOCATOR_CANDIDATES_COUNT, time=3).text
        return int(data)
