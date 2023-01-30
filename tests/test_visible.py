import time

from page.demoqa import Demoqa
from page.elements_page import ElementsPage

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()
    elements_page.btn_sidebar_first_click()
    time.sleep(3)
    assert elements_page.btn_sidebar_first_textbox.not_visible()