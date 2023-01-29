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
        self.find_element().click()

    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
    def get_text(self):
        return str(self.find_element().text)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.find_element().is_displayed()

    def not_visible(self, time_wait=2):

        try:
            WebDriverWait(self.driver, time_wait).until_not(EC.invisibility_of_element((By.CSS_SELECTOR, self.locator)))
            return False
        except TimeoutException:
            return True
