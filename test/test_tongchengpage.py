# -*- encoding:utf-8 -*-
import unittest
from pageobject.tongchengpage import TongChengPage,Join_in_beijin
from utils.loginpage import LoginPage

class TestTongChengPage(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            email = '382135230@qq.com'
            password = "Ljc960614"
            login = LoginPage()
            login.open_and_check()
            login.login(email, password)

        def test_tongchengpage(self):
            TongChengPage().open_and_check()

        def test_join_beijin(self):
            Join_in_beijin().open_and_check()

if __name__ == '__main__':
    unittest.main()
