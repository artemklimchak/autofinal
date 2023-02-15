import pytest
from pages.auth_page import AuthPage

def test_authorisation_phone(web_browser):

    page = AuthPage(web_browser)
    button_element = driver.find_element_by_id("t-btn-tab-phone")

    button_element.click()
    page.email.send_keys('89872909354')

    page.password.send_keys("Nba@2023")

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

def test_authorisation_mail(web_browser):

    page = AuthPage(web_browser)
    button_element = driver.find_element_by_id("t-btn-tab-mail")

    button_element.click()
    page.email.send_keys('89872909354@rambler.ru')

    page.password.send_keys("Nba@2023")

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

def test_authorisation_login(web_browser):

    page = AuthPage(web_browser)
    button_element = driver.find_element_by_id("t-btn-tab-login")

    button_element.click()
    page.email.send_keys('89872909354')

    page.password.send_keys("Nba@2023")

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_authorisation_ls(web_browser):
    page = AuthPage(web_browser)
    button_element = driver.find_element_by_id("t-btn-tab-ls")

    button_element.click()
    page.email.send_keys('89872909354')

    page.password.send_keys("Nba@2023")

    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

