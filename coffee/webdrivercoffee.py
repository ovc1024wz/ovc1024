# encoding:utf-8

from webdriver import driver

class CoffeePage():
    url = None
    page_flag_xpath = None
    page_flag_keyword = None

    def __init__(self):
        self.driver = driver

    def open_and_check(self):
        self.driver.get(self.url)
        return self.check_if_page_opened()
    def check_if_page_opened(self):

        act_keyword = self.driver.find_element_by_xpath(self.page_flag_xpath).text

        if act_keyword == self.page_flag_keyword:
            return True
        else:
            return False
