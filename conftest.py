from selenium import webdriver
import pytest


@pytest.fixture(scope='module')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

