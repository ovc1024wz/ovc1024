# -*-encoding:utf-8-*-
import unittest
from utils.loginpage import LoginPage
from pageobject.userspage import UsersPage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loginpage = LoginPage()
        email = "763208734@qq.com"
        password = "yu75321ysq"
        loginpage.open_and_check()
        loginpage.login(email, password)

    def test_something(self):
        UsersPage().open_and_check()
        self.assertEqual(True, UsersPage().open_and_check())


if __name__ == '__main__':
    unittest.main()