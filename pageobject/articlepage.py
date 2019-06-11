# -*-encoding:utf-8-*-
import time
from coffee.webdriver import driver
from coffee.webdrivercoffee import CoffeePage
from utils.urls import ARTICLE_PAGE_URL

class ArticlePage(CoffeePage):
    url = ARTICLE_PAGE_URL
    page_flag_xpath = "/html/body/div[3]/div[2]/div[2]/div[1]/div[1]"
    page_flag_keyword = u"推荐阅读"

    def publisharticles(self):
        publish_articles_url = "/html/body/div[3]/nav/a"
        driver.find_element_by_xpath(publish_articles_url).click()

        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div[1]/input").send_keys(u"测试1")
        time.sleep(1)
        driver.find_element_by_class_name("w-e-text").send_keys(u"测试2")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div[3]/textarea").send_keys(u"测试3")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div[4]/input").send_keys(u"测试4")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/button").click()

    def checkarticles(self):
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/a").click()

    def choosepage(self):
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[11]/nav/ul/li[2]/a").click()

    def all(self):
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/a").click()