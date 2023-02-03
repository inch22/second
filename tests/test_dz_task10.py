from page.allerts_page import Alerts
from page.modal_page import Modal
from page.elements_page import ElementsPage



# задача 1
def test_elements_dz(browser):
    modal = Modal(browser)
    modal.visit()
    assert modal.btn_modal_menu.check_count_elements(5)


# задача 2
def test_navigation_dz(browser):
    modal = Modal(browser)
    modal.visit()
    browser.refresh()
    modal.btn_allerts_menu.click_elem()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    elements_page = Alerts(browser)
    assert elements_page.equal_url()
    browser.set_window_size(1000, 1000)
