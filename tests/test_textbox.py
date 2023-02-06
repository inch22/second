from page.textbox_page import TextboxPage
from page.elements_page import ElementsPage
import time
from selenium.webdriver.common.keys import Keys


def test_name_address(browser):
    text1 = TextboxPage(browser)
    text1.visit()
    text1.full_name.send_keys('Ivanov Ivan')
    time.sleep(2)
    text1.current_address.send_keys('Spb, Dostoevskaya str., 9')
    text1.btn_submit.click_elem()
    time.sleep(2)

    assert text1.name_text.get_text() == 'Name:Ivanov Ivan'
    assert text1.address_text.get_text() == 'Current Address :Spb, Dostoevskaya str., 9'