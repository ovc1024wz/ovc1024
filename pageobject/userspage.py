# -*-encoding:utf-8-*-
from coffee.webdrivercoffee import CoffeePage
from utils.urls import USERS_PAGE_URL

class UsersPage(CoffeePage):
    url = USERS_PAGE_URL
    page_flag_xpath = "/html/body/div[3]/div/div[2]/dl/dd/div/span"
    page_flag_keyword = u"关注数"

