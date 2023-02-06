from page.form_page import FormPage
from page.elements_page import ElementsPage
import time
from selenium.webdriver.common.keys import Keys

def test_login_form(browser):
    forma = FormPage(browser)
    forma.visit()
    assert not forma.modal_dialog.exist()
    time.sleep(2)
    forma.first_name.send_keys("tester")
    forma.last_name.send_keys("testerovich")
    forma.user_email.send_keys("test@ttt.tt")
    forma.gender_radio_1.click_forse()
    forma.user_number.send_keys("9992223344")
    time.sleep(2)
    forma.user_email.send_keys(Keys.COMMAND + "a")
    time.sleep(2)
    forma.user_email.send_keys(Keys.DELETE)
    time.sleep(2)
    # forma.btn_submit.click_forse()
    # time.sleep(2)
    # assert forma.modal_dialog.exist()
    # forma.btn_close_modal.click_forse()

    #ДЗ
    forma.hobbies_checkbox_1.click_forse()
    time.sleep(2)
    forma.current_address.send_keys("Russia, Spb, Dostoevskaya str., 9")
    time.sleep(2)
