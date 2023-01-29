from page.demoqa import Demoqa
from page.elements_page import ElementsPage


def test1_go_to_page_elements(browser):
    b = Demoqa(browser)
    c = ElementsPage(browser)

    b.visit()
    #assert b.equal_url()
    #b.btn_elements.click()
    #assert c.equal_url()
