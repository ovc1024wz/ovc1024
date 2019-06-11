# -*- encoding:utf-8 -*-

from coffee.webdrivercoffee import CoffeePage
from utils.urls import TONGCHENG_PAGE_URL,BEIJING_PAGE_URL

class TongChengPage(CoffeePage):
        url = TONGCHENG_PAGE_URL
        page_flag_xpath = "//div[@class='card-header']"
        page_flag_keyword = u"选择加入同城"

class  Join_in_beijin(CoffeePage):
        url = BEIJING_PAGE_URL
        page_flag_xpath = "//div[@class='info']"
        page_flag_keyword = u'北京'

