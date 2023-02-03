from page.base_page import BasePage
from components.components import WebElement

class Modal(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_modal_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.btn_allerts_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li#item-1')


