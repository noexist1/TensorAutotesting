from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser 

    def find_element(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)

    def switch_to_new_window(self):
        windows = self.browser.window_handles
        new_window = windows[-1]
        return self.browser.switch_to.window(new_window)
    
    def attribute(self, element, attribute_name):
        #element = self.find_element()
        return element.get_attribute(attribute_name)
    
    def get_current_url(self):
        return self.browser.current_url
    
    def get_page_title(self):
        return self.browser.title
    