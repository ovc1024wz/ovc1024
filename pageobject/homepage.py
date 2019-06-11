# encoding:utf-8

from coffee.webdrivercoffee import CoffeePage
from utils.urls import HOME_PAGE

class HomePage(CoffeePage):
    url = HOME_PAGE
    page_flag_xpath = "/html/body/div[3]/div[3]/div[1]/div[1]/div[1]"
    page_flag_keyword = u"最新签到用户"
