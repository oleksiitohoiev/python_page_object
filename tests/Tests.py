from tests.DjinniPages import HomeHelper
from tests.DjinniPages import SearchHelper


def test_value_vacancies_more_than_candidates(browser):
    main_page = HomeHelper(browser)
    main_page.go_to_site()
    main_page.click_on_the_salary_button()
    search_page = SearchHelper(browser)
    search_page.click_on_the_aqa_filter()
    assert search_page.check_aqa_title()
    search_page.click_exp_filter()
    assert search_page.value_vacancies() > search_page.value_candidates()
