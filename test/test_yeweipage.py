import unittest
from pageobject.yeweipage import YeWeiPage
from utils.loginpage import LoginPage
import time
class TestYeWeiPage(unittest.TestCase):

      @classmethod
      def setUpClass(cls):
          email = '1301918819@QQ.COM'
          password = 'zyq123'
          LoginPage().open_and_check()
          LoginPage().login(email, password)
          time.sleep(3)

      def test_open_yewei_page(self):
          self.assertTrue(YeWeiPage().open_and_check())

if __name__ == '__main__':
    unittest.main()

