import time
from page.textbox_page import TextboxPage


@allure.feature('check attr')
@allure.story('проверка значения атрибута элемента')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    """ проверка значения атрибута элемента """
    atrb1 = TextboxPage(browser)
    atrb1.visit()
    assert atrb1.full_name.get_dom_attribute('placeholder') == 'Full Name'

@allure.feature('check attr')
@allure.story('проверка наличия атрибута элемента')
@allure.severity(allure.severity_level.BLOCKER)
def test_attr_exist(browser):
    """ проверка наличия атрибута элемента """
    atrb2 = TextboxPage(browser)
    atrb2.visit()
    atrb2.btn_first.click_elem()
    assert atrb2.box_first_menu.get_dom_attribute('style')

@allure.feature('check attr')
@allure.story('проверка отсутствия атрибута элемента')
@allure.severity(allure.severity_level.BLOCKER)
def test_attr_not_exist(browser):
    """ проверка отсутствия атрибута элемента """
    atrb3 = TextboxPage(browser)
    atrb3.visit()
    atrb3.btn_first.click_elem()
    assert not atrb3.btn_first.get_dom_attribute('style')

