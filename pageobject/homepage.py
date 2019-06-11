# encoding:utf-8

from coffee.webdrivercoffee import CoffeePage
from utils.urls import HOME_PAGE,HOME_PAGE_FABIAO


class HomePage(CoffeePage):
    url = HOME_PAGE
    page_flag_xpath = "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]"
    page_flag_keyword = u"最新签到用户"



class FaBiao(CoffeePage):
    def say_input(self):
        say = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/textarea")
        say.send_keys(u"心情很复杂")
        send = self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[2]/div/div[1]/form/input[2]")
        send.click()
class FaBiao_Flag(CoffeePage):
    url = HOME_PAGE_FABIAO
    page_flag_xpath = "/html/body/div[3]/div/div[1]/div[3]/div[1]"
    page_flag_keyword = u"更多wzyuchen的唠叨"