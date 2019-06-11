# encoding=utf-8
from coffee.webdriver import driver
from coffee.webdrivercoffee import CoffeePage
from utils.urls import laodao_url,laodao_page_flag_xpath,laodao_keyword ,write_laodao_xpth,delete_laodao_xpth
from utils.urls import answerlaodao_tiaozhuan_xpth,answer_write_laodao_xpth,answer_write_laodao_click_xpth,visit_other_laodao_url
class LaoDao(CoffeePage):
    url=laodao_url
    page_flag_xpath=laodao_page_flag_xpath
    page_flag_keyword=laodao_keyword
    def __init__(self):
        self.driver=driver
    def write_laodao(self):
        self.driver.find_element_by_id("content").send_keys("nihahhhhhhhhhhhh")
        self.driver.find_element_by_xpath(write_laodao_xpth).click()
    def delete_laodao(self):
        self.driver.find_element_by_xpath(delete_laodao_xpth).click()
    def answer_laodao(self):
        self.driver.find_element_by_xpath(answerlaodao_tiaozhuan_xpth).click()
        self.driver.find_element_by_xpath(answer_write_laodao_xpth).send_keys("1234567234534534")
        self.driver.find_element_by_xpath(answer_write_laodao_click_xpth).click()
    def visit_other_laodao(self):
        self.driver.find_elements_by_xpath(visit_other_laodao_url)
