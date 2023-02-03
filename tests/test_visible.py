import time

from page.demoqa import Demoqa
from page.elements_page import ElementsPage
from page.accordion_page import Accordion

#занятие 9
def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()
    elements_page.btn_sidebar_first.click_elem()
    time.sleep(3)
    assert elements_page.btn_sidebar_first_textbox.not_visible()


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.one_paragraph.visible()
    accordion_page.one_section_btn.click_elem()
    time.sleep(2)
    assert accordion_page.one_paragraph.not_visible()


#занятие 10
def test_visible_default_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.one_paragraph.visible()
    accordion_page.one_section_btn.click_elem()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    assert accordion_page.one_paragraph.not_visible()
    browser.refresh()
    browser.set_window_size(1000, 1000)
    assert accordion_page.one_paragraph.visible()


#занятие 11
def test_not_exist(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.not_elem.exist()


