from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class SabyContactsPage(BasePage):
    URL = 'https://saby.ru/contacts/54-novosibirskaya-oblast?tab=clients'

    BANNER_TENSOR = (By.CSS_SELECTOR, '#contacts_clients a[href="https://tensor.ru/"]')
    TITLE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title')
    BUTTON_MORE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg a[href="/about"]')


    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(self.URL)

    def click_banner(self):
        banner = self.find_element(self.BANNER_TENSOR)
        return banner.click()

    def find_title(self):
        return self.find_element(self.TITLE)

    @property
    def title_text(self):
        return self.find_title().text
    
    def click_button_more(self):
        button_more = self.find_element(self.BUTTON_MORE)
        return button_more.click()
    
    @property
    def current_url(self):
        return self.browser.current_url
    


