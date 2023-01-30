from selenium.webdriver.common.by import By
from page.demoqa import Demoqa

def test_icon_exist(browser):
    icona = Demoqa(browser)
    icona.visit()
    icona.icon.click_elem()
    assert icona.equal_url()
    assert icona.icon.exist()





