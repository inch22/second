from selenium.common.exceptions import NoSuchElementException
from page.base_page import BasePage
from components.components import WebElement


class Demoqa(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        super().__init__(driver, self.base_url)

