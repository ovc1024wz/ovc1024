# -- encoding:utf-8 --
import unittest
import time
from utils.loginpage import LoginPage
from pageobject.mycommunity import MyCommPage, CreateTream

class TestMyComm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        email = '15707205332@163.com'
        password = 'zsh971220'
        loginPage = LoginPage()
        loginPage.open_and_check()
        loginPage.login(email, password)

    def test_mycomm_page(self):
        mycommunity = MyCommPage()
        mycommunity.open_and_check()
        self.assertTrue(mycommunity.check_if_page_opened())
        time.sleep(3)

        team_element = mycommunity.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-info float-right']")
        team_element.click()

    def test_create_team_page(self):
        createtream = CreateTream()
        createtream.open_and_check()
        self.assertTrue(createtream.check_if_page_opened())


if __name__ == '__main__':
    unittest.main()
