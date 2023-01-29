from page.demoqa import Demoqa
from page.elements_page import ElementsPage


# def test_check_text_please(browser):
#     icona1 = Demoqa(browser)
#     elements_page = ElementsPage(browser)
#     icona1.visit()
#     icona1.btn_elements.click_elem()
#     assert elements_page.text_please.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_please.get_text() == 'Please select an item from left to start practice.'
    assert elements_page.text_element.get_text() == 'Elements'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()
