
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url #"https://demoqa.com/"

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        self.locator = locator
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url

