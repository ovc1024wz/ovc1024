# -*- encoding:utf-8 -*-

from utils.loginpage import LoginPage
from utils.urls import SEARCH_PAGE
from coffee.webdrivercoffee import CoffeePage




email = '958022706@qq.com'
password = '8763366'
login = LoginPage()
login.open_and_check()
login.login(email,password)



class SeachPage(CoffeePage):

    url = SEARCH_PAGE
    page_flag_xpath = "//div[@class='c9 mt-3 ml-3 fs12']"
    page_flag_keyword = u"标题模糊搜索"

    page_flag_search = None

    def input_keywords(self,word):
        input_keywords = self.driver.find_element_by_xpath("//input[@class='form-control']")
        input_keywords.send_keys(word)
        button_login = self.driver.find_element_by_xpath("//button[@type='submit']")
        button_login.click()


    def check_if_search_true(self):
        output_words = self.driver.find_element_by_xpath("//div[@class='s_top']")
        print("[DEBUG:%s" % output_words.text)
        if  output_words.text == self.page_flag_search:
            return True
        else:
            return False



