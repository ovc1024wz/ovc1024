# encoding:utf8
from utils.loginpage import LoginPage
from utils.urls import ALBUM_PAGE_URL
from utils.urls import ALBUM_PAGE_GROUP_URL

class AlbumPage(LoginPage):
    url=ALBUM_PAGE_URL
    page_flag_xpath='//div[@class="mb-3"]/a'
    page_flag_keyword=u'最新相册'


class AlbumGroup(LoginPage):
    url=ALBUM_PAGE_GROUP_URL
    page_flag_xpath='//a[@class="btn btn-sm text-secondary"]'
    page_flag_keyword=u'最新相册'










