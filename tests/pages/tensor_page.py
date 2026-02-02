from selenium.webdriver.common.by import By
from pages.base_page import BasePage




class TensorPage(BasePage):
    PICTURES = (By.XPATH, '//h2[text()="Работаем"]/ancestor::div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//div[2]//img')
    
    def __init__(self, browser):
        super().__init__(browser)

    def find_pictures(self):
        return self.find_elements(self.PICTURES)
    
    @property
    def excepted_width(self):
        pictures = self.find_pictures()
        return self.attribute(pictures[0], 'width')

    @property
    def excepted_height(self):
        pictures = self.find_pictures()
        return self.attribute(pictures[0], 'height')

    