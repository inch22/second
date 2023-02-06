from page.textbox_page import TextboxPage
import time



def test_name_address(browser):
    text1 = TextboxPage(browser)
    text1.visit()
    #browser.set_window_size(1200, 1500)
    text1.full_name.send_keys('Ivanov Ivan')
    time.sleep(2)
    text1.current_address.send_keys('Spb, Dostoevskaya str., 9')
    text1.btn_submit.click_forse()
    time.sleep(5)

    assert text1.name_text.get_text() == 'Name:Ivanov Ivan'
    assert text1.address_text.get_text() == 'Current Address :Spb, Dostoevskaya str., 9'