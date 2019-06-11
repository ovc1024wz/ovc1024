# -*-encoding:utf-8-*-
import unittest
from utils.loginpage import LoginPage
from pageobject.articlepage import ArticlePage
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        LoginPage().open_and_check()
        LoginPage().login("1509032044@qq.com", "rqw12590")

    def setUp(self):
        ArticlePage().open_and_check()
    #测试页面是否打开
    def test_articlepage_open(self):
        TF = ArticlePage().open_and_check()
        self.assertEqual(True, TF)
    #发布文章
    def test_publish_articles(self):
        ArticlePage().publisharticles()
    #查看文章
    def test_check_articles(self):
        ArticlePage().checkarticles()
     #选择分页
    def test_choose_page(self):
        ArticlePage().choosepage()
    #全部文章
    def test_all(self):
        ArticlePage()

if __name__ == '__main__':
    unittest.main()
