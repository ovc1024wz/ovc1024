#encoding=utf-8
import unittest,time
from coffee.webdriver import driver
from utils.loginpage import LoginPage
from pageobject.laodao import LaoDao
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        email = "2589240188@qq.com"
        password = "123456"
        LoginPage().open_and_check()
        LoginPage().login(email, password)
    def setUp(self):
        LaoDao().open_and_check()
        self.assertEqual(True, LaoDao().check_if_page_opened())
    def test_laodao1(self):
        # 删除列表中的该条唠叨
        LaoDao().delete_laodao()
        time.sleep(5)
    def test_laodao2(self):
        # 回复列表中的该条唠叨
        LaoDao().answer_laodao()
        time.sleep(5)
    def test_laodao3(self):
        # 唠叨框中填写信息
        LaoDao().write_laodao()
        time.sleep(5)
    def test_laodao4(self):
        # 查看别人的唠叨
        LaoDao().visit_other_laodao()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
