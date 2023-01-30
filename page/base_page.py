
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url #"https://demoqa.com/" базовая страница

    def visit(self):
        return self.driver.get(self.base_url) #возвращает переход на страницу

    def back(self):
        self.driver.back() #стрелка назад в браузере

    def forward(self):
        self.driver.forward() #стрелка вперед в браузере

    def refresh(self):
        self.driver.refresh() #обновить страницу

    def get_url(self):
        return self.driver.current_url #получить текущий url

    def get_title(self):
        return self.driver.title #получить title  страницы

    def equal_url(self): #метод должен вызывать get_url сравнивать его со строкой 'https://demoqa.com/'
                         #возвращать True если проверка пройдена и False если нет
        if self.get_url() == self.base_url:
            return True
        return False



