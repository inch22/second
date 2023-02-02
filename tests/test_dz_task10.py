import time
from page.modal_page import Modal
from page.elements_page import ElementsPage

# задача 1
def test_elements_dz(browser):
    modal = Modal(browser)
    elements_page = ElementsPage(browser)
    modal.visit()
    assert elements_page.btn_modal_menu.check_count_elements(5)

# задача 2
def test_navigation_dz(browser):
    modal = Modal(browser)
    elements_page = ElementsPage(browser)
    modal.visit()
    browser.refresh()
    elements_page.btn_allerts_menu.click_elem()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert elements_page.get_url()
    browser.refresh()
    browser.set_window_size(1000, 1000)
