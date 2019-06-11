#encoding:utf-8
from utils.urls import YEWEI_PAGE_URL
from coffee.webdrivercoffee import CoffeePage

class YeWeiPage(CoffeePage):

      url = YEWEI_PAGE_URL
      page_flag_xpath = "/html/body/div[3]/div/div[2]/div/div/h1"
      page_flag_keyword = u'关于我们'