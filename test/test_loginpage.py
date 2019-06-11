# -*- encoding:utf-8 -*-
import unittest
from utils.loginpage import LoginPage

class TestLoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_page = LoginPage()

    def test_page_open(self):
        self.assertEqual(True,self.login_page.open_and_check())

    def test_page_open(self):
        email = '85947557@qq.com'
        password = '123456789'
        self.login_page.open_and_check()
        self.login_page.login(email,password)


if __name__ == '__main__':
    unittest.main()
