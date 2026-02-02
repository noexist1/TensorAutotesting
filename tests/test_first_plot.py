from pages.saby_page import SabyPage 
from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_page import TensorPage



def test_go_to_contacts(browser):
    saby_page = SabyPage(browser)
    saby_page.open()
    saby_page.find_invisible_element()
    saby_page.click_contact_link()


def test_check_title_text(browser):
    saby_contacts_page = SabyContactsPage(browser)
    saby_contacts_page.click_banner()
    saby_contacts_page.switch_to_new_window()
    saby_contacts_page.find_title()
    assert saby_contacts_page.title_text == 'Сила в людях', 'Title name is not found'


def test_check_matching_urls(browser):
    saby_contacts_page = SabyContactsPage(browser)
    saby_contacts_page.click_button_more()
    excepted_url = 'https://tensor.ru/about'
    current_url = saby_contacts_page.get_current_url()
    assert current_url == excepted_url, 'Current url does not match expected url'
    

def test_check_pictures_size(browser):
    tensor_page = TensorPage(browser)
    pictures = tensor_page.find_pictures()
    excepted_width = tensor_page.excepted_width
    excepted_height = tensor_page.excepted_height
    print(excepted_height, excepted_width)
    for p in pictures:
        assert tensor_page.attribute(p, 'width') == excepted_width and tensor_page.attribute(p, 'height') == excepted_height


    


