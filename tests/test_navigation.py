from page.demoqa import Demoqa
from page.elements_page import ElementsPage


def test_navigation(browser):
    navi = Demoqa(browser)
    elements_page = ElementsPage(browser)
    navi.visit()
    navi.btn_elements.click_elem()

    elements_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()
