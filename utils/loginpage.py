# -*-encoding:utf-8-*-
from coffee.coffeepage import CoffeePage
from utils.urls import LOGIN_PAGE_URL

class LoginPage(CoffeePage):
    url = LOGIN_PAGE_URL
    page_xpath = "//div[@class='fs24']"
    page_flag_keyword = u"用户登录"

    @property
    def email_input(self):
        name = 'email'
        email_input_element = self.driver.find_element_by_name(name)
        return email_input_element

    @property
    def password_input(self):
        name = 'pwd'
        password_input_element = self.driver.find_element_by_name(name)
        return password_input_element

    @property
    def submit(self):
        __id = 'comm-submit'
        submit_element = self.driver.find_element_by_id(__id)
        return submit_element

    def login(self, email, password):
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.submit.click()
