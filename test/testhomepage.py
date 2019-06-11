# encoding:utf-8
import unittest
from pageobject.homepage import HomePage,FaBiao,FaBiao_Flag
from utils.loginpage import LoginPage
class TestHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        email = "896417651@qq.com"
        password = "w896417651"
        LoginPage().open_and_check()
        LoginPage().login(email,password)
    def test_homepage(self):
        HomePage().open_and_check()
        self.assertTrue(HomePage().open_and_check())

    def test_say(self):
        FaBiao().say_input()
        FaBiao_Flag().open_and_check()
        self.assertTrue(FaBiao_Flag().open_and_check())






if __name__ == '__main__':
    unittest.main()
