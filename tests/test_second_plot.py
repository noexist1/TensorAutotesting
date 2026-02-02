from pages.saby_page import SabyPage


def test_check_current_region(browser):
    saby_page = SabyPage(browser)
    saby_page.open()
    saby_page.find_invisible_element()
    saby_page.click_contact_link()
    assert saby_page.name_region == "Новосибирская обл.", 'Uncorrect region'


partners = []
def test_check_partners(browser):
    saby_page = SabyPage(browser)
    partners = saby_page.get_partners()
    assert saby_page.partners_city_name == 'Новосибирск', 'Uncorrect city name'
    assert len(partners) > 0, 'Amount of partners is 0' 


def test_change_region(browser):
    saby_page = SabyPage(browser)
    saby_page.click_to_change_region()
    saby_page.change_region()
    assert saby_page.check_changed_region(), 'region is not changed'


def test_updates_of_change(browser):
    saby_page = SabyPage(browser)
    new_partners = saby_page.get_partners()
    assert new_partners != partners, 'list of partners is not changed'
    current_url = saby_page.get_current_url()
    assert 'kamchatskij' in current_url, 'url is not changed'
    page_title = saby_page.get_page_title()
    assert 'Камчатский' in page_title, 'title is not changed'

