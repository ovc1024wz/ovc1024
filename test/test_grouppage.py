# -*- encoding:utf-8 -*-
import unittest
from utils.loginpage import LoginPage
from pageobject.grouppage import UserGroupPage
import time
class TestUserGroupPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        username = '85947557@qq.com'
        password = '123456789'
        LoginPage().open_and_check()
        LoginPage().login(username,password)
        time.sleep(5)

    def test_open_user_group_page(self):
        UserGroupPage().open_and_check()


if __name__ == '__main__':
    unittest.main()
