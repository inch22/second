from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click_elem(self):
        self.find_element().click() #действие, нажимает на кнопку

    def find_element(self): #ищет элемент
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self): #ищет элементы по неуникальному локатору
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int): #проверка количество элемнтов списка

        if len(self.find_elements()) == count:
            return True
        return False


    def get_text(self): #возвращает текст
        return str(self.find_element().text)

    def exist(self): #проверяет наличие элемента
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self): # проверяет видимость элемента
        return self.find_element().is_displayed()

    def not_visible(self, time_wait=2):  #метод проверяет, что элемент не виден

        try:
            WebDriverWait(self.driver, time_wait).until_not(EC.invisibility_of_element((By.CSS_SELECTOR, self.locator)))
            return False
        except TimeoutException:
            return True

    def send_keys(self, text: str): #метод ввода текст в поле
        self.find_element().send_keys(text)

    def click_forse(self): #метод принудительного нажатия
        self.driver.execute_script("arguments[0].click();", self.find_element())



