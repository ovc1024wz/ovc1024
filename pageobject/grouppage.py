# -*- encoding:utf-8 -*-
from coffee.webdrivercoffee import CoffeePage
from utils.urls import USEGROUP_PAGE_URL

class UserGroupPage(CoffeePage):

    url = USEGROUP_PAGE_URL
    page_flag_xpath = "//nav[@class='position-relative']/a"
    page_flag_keyword = u"创建小组"