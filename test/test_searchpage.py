# -*- encoding:utf-8 -*-

import unittest
from pageobject.searchpage import SearchPage


class DemoSearchPage(SearchPage):
    page_flag_search = u"获得约 9 条结果"


class TestSearchPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.search = DemoSearchPage()

    def test_open_and_check(self):
        self.assertTrue( self.search.open_and_check())

    def test_search_keywords(self):
        self.search.open_and_check()
        self.search.input_keywords('11')
        self.assertTrue(self.search.check_if_search_true())



if __name__ == '__main__':
    unittest.main()
