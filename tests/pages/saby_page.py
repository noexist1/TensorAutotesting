from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyPage(BasePage):
    URL = "https://saby.ru/"

    CONTACT_ELEMENT = (By.CLASS_NAME, 'sbisru-Header__menu-item-1')
    CONTACT_LINK = (By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu a[href="/contacts"]')

    REGION_NAME_BUTTON = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--xm12"]//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    PARTNERS_CITY_NAME = (By.XPATH, '//div[@id="contacts_clients"]//div[@name="itemsContainer"]//div[@id="city-id-2"]')
    PARTNERS = (By.XPATH, '//div[@id="contacts_clients"]//div[@name="itemsContainer"]/div[@item-parent-key]')
    EXCEPTED_REGION = (By.CSS_SELECTOR, "[title='Камчатский край']")

    
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get(self.URL)

    def find_invisible_element(self):
        element = self.find_element(self.CONTACT_ELEMENT)
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()

    def click_contact_link(self):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.CONTACT_LINK)).click()

    @property
    def name_region(self):
        region = self.find_element(self.REGION_NAME_BUTTON)
        return region.text
    
    @property
    def partners_city_name(self):
        city_name = self.find_element(self.PARTNERS_CITY_NAME)
        return city_name.text

    def get_partners(self):
        partners = self.find_elements(self.PARTNERS)
        return partners
    
    def click_to_change_region(self):
        button_region = self.find_element(self.REGION_NAME_BUTTON)
        button_region.click()

    def change_region(self):
        iframes = self.browser.find_elements(By.TAG_NAME, "iframe")
        if iframes:
            self.browser.switch_to.frame(iframes[0])

        new_region = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.EXCEPTED_REGION))
        new_region.click()
        self.browser.switch_to.default_content()

    def check_changed_region(self):
        result = WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element((self.REGION_NAME_BUTTON), 'Камчатский край'))
        return result
    
        


