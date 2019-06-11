# encoding:utf8
import unittest
from pageobject.album_page import AlbumPage,AlbumGroup
from utils.loginpage import LoginPage
import time

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        email = '2810413349@qq.com'
        password = '970213cb19'
        login = LoginPage()
        login.open_and_check()
        login.login(email,password)

    def test_something(self):
        album=AlbumPage()
        album.open_and_check()
        time.sleep(3)
        chech=album.driver.find_element_by_xpath('//a[@style="z-index: 100;top:6px;right:6px;"]')
        chech.click()
        time.sleep(3)
        album_group=AlbumGroup()
        album_group.open_and_check()




if __name__ == '__main__':
    unittest.main()
