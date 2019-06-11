# -- encoding:utf-8 --
from coffee.webdrivercoffee import CoffeePage


class MyCommPage(CoffeePage):

    url = "http://47.92.220.226/bbs/index.php/my"
    page_flag_xpath = "//div[@class='col-md-9']/div[1]/div[1]"
    page_flag_keyword = u"我的小组"

class CreateTream(CoffeePage):
    url = "http://47.92.220.226/bbs/index.php/group/create"
    page_flag_xpath = "//form[@role='form']/div[1]/label"
    page_flag_keyword = u"小组名称"

