from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=ztrFM_dv24M'
        super().__init__(web_driver, url)

    name = WebElement(name='firstName')
    lastname = WebElement(name='lastName')
    mail = WebElement(id='address')
    password = WebElement(id='password')
    passwordconf = WebElement(id='password-confirm')

    btn = WebElement(id='register')