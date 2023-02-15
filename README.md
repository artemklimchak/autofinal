
conftest.py contains all the required code to catch failed test cases and make screenshot of the page in case any test case will fail.

pages/base/registration.py contains PageObject pattern implementation for Python.

pages/elements.py contains helper class to define web elements on web pages.

How To Run Tests
Install all requirements:

pip install -r requirements

Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

Run tests:

python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*

Примененные техники тест-дизайна:  метод граничных значений (длина пароля, фамилии, имени), предугадывание ошибок (е-мейл без указания @, домена, отправка пустых данных, пробелов и т.п.) , попарное тестирование.
