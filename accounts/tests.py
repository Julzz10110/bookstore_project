from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase

import time

class CustomerListTestCase(LiveServerTestCase):

    def setUp(self):
        self.client.login(username="user1", password="password![135]")
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.selenium.get('http://127.0.0.1:8000/')
        super(CustomerListTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(CustomerListTestCase, self).tearDown()

    def test_succesful_login(self, username='user1', password='password![135]', next_url=None):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username_el = self.selenium.find_element(By.NAME, 'login')
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.NAME, 'password')
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.XPATH, '//button[text()="Войти"]')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        assert 'Добро пожаловать, user1@mail.ru!' in self.selenium.page_source

    def test_unsuccesful_login(self, username='fakeuser', password='fakepassword', next_url=None):
        self.selenium.get('http://127.0.0.1:8000/accounts/login/')
        username_el = self.selenium.find_element(By.NAME,'login')
        username_el.send_keys(username)
        password_el = self.selenium.find_element(By.NAME,'password')
        password_el.send_keys(password)
        submit = self.selenium.find_element(By.XPATH, '//button[text()="Войти"]')
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        assert 'Имя пользователя и/или пароль не верны.' in self.selenium.page_source

