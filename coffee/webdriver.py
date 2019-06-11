# encoding:utf-8
from selenium import webdriver
from abs import Singleton

@Singleton
class WebDriver():

    driver = None

    def __init__(self):
        if self.driver == None:
            self.driver = webdriver.Firefox()

    def get_driver(self):
        return self.driver

driver = WebDriver().get_driver()
