from page.base_page import BasePage
from components.components import WebElement


class TextboxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress.form-control')
        self.btn_submit = WebElement(driver, '#submit')
        self.name_text = WebElement(driver, '#name')
        self.address_text = WebElement(driver, '#currentAddress.mb-1')
        self.box_first_menu = WebElement(driver, locator="div.row > div:nth-child(1) > div > div > div:nth-child(1) > div")
        self.btn_first = WebElement(driver, locator="div > div > div:nth-child(1) > span")

