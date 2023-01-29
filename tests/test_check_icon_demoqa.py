from selenium.webdriver.common.by import By
from page.demoqa import Demoqa

def test_icon_exist(browser):
    icona = Demoqa(browser)
    icona.visit()
    icona.icon.click_elem()
    #assert icona.equal_url()
    #assert icona.icon.exist()





    # browser.get('https://demoqa.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #      print("Элемент не найден")
    # else:
    #      print("Элемент найден")

