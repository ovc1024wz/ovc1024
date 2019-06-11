import unittest

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
        MyCommPage().open_and_check()
        # self.assertEqual(True, False)

    def test_create_team_page(self):
        CreateTream().open_and_check()

    # def test_team(self):
    #     button = self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-info float-right']")
    #     button.click()




if __name__ == '__main__':
    unittest.main()
