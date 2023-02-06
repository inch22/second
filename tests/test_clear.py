from page.base_page import BasePage
import time
from page.textbox_page import TextboxPage


def test_clear(browser):
    clear1 = TextboxPage(browser)
    clear1.visit()
    clear1.full_name.send_keys('Ivanov Ivan')
    time.sleep(2)
    clear1.full_name.clear()
    time.sleep(2)
    assert clear1.full_name.get_text() == ''