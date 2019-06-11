# -- encoding:utf-8 --
from coffee.webdrivercoffee import CoffeePage
from utils.urls import SHEQU_PAGE_URL, CREATETEAM_PAGE_URL

class MyCommPage(CoffeePage):

    url = SHEQU_PAGE_URL
    page_flag_xpath = "//div[@class='col-md-9']/div[1]/div[1]"
    page_flag_keyword = u"我的小组"

class CreateTream(CoffeePage):
    url = CREATETEAM_PAGE_URL
    page_flag_xpath = "//form[@role='form']/div[1]/label"
    page_flag_keyword = u"小组名称"

