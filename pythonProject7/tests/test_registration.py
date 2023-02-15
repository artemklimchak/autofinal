def test_registration_empty(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys(' ')
    page.lastname.send_keys(' ')
    page.mail.send_keys(' ')
    page.password.send_keys(" ")
    page.passwordconf.send_keys(" ")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_valid(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys('89872909354')
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_nameinvalid(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Ben')
    page.lastname.send_keys('Stiller')
    page.mail.send_keys('89872909354')
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

def test_registration_nameinvalid1(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('B')
    page.lastname.send_keys('S')
    page.mail.send_keys('89872909354')
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

def test_registration_nameinvalid2(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Be')
    page.lastname.send_keys('St')
    page.mail.send_keys('89872909354')
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_nameinvalid3(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('111')
    page.lastname.send_keys('222')
    page.mail.send_keys('89872909354')
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_invalidmail(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys("89872909354@mail")
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'

def test_registration_invalidtel(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys("8987290935")
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_invalidtel2(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys("8987290935te")
    page.password.send_keys("Nba@2023")
    page.passwordconf.send_keys("Nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_invalidpassw(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys("89872909354")
    page.password.send_keys("Nba2023")
    page.passwordconf.send_keys("Nba2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'


def test_registration_invalidpassw2(web_browser):

    page = AuthPage(web_browser)

    page.name.send_keys('Чарльз')
    page.lastname.send_keys('Баркли')
    page.mail.send_keys("89872909354")
    page.password.send_keys("nba@2023")
    page.passwordconf.send_keys("nba@2023")
    page.btn.click()

    assert page.get_current_url() == 'https://b2c.passport.rt.ru/account_b2c/page?state=a81509d3-01a7-42ce-894b-39cc4db959b5&client_id=account_b2c&theme=light#/'
