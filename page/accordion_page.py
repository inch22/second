from page.base_page import BasePage
from components.components import WebElement
from page.elements_page import ElementsPage

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.one_section_btn = WebElement(driver, '#section1Heading')
        self.one_paragraph = WebElement(driver, '#section1Content > p')