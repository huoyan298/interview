# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    :
# @File    : 
# @Software: PyCharm
from pom.BasePage.basepage import basepage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage(basepage):
    url='https://www.baidu.com'
    user=(By.NAME,'accounts')
    password=(By.NAME,'pwd')
    login_button=(By.XPATH,'//*[@id="s_btn_wr"]')
    search_btn = (By.XPATH, '//*[@id="su"]')
    search_world=(By.XPATH,'//*[@id="kw"]')
    # txt=""
    # def __init__(self,driver,txt):
    #     self.driver=driver
    #     self.txt =txt
    # @classmethod
    def search(self,search_world,txt):
        self.visit()
        self.input_txt(self.search_world,txt)

    def login(self,usename,pwd):
        self.visit()
        self.input_txt(self.user,usename)
        # self.input_(self.password,pwd)
        self.click(self.login_button)

if __name__=="__main__":
    driver=webdriver.Firefox()
    txt= "你好"
    l=LoginPage(driver)
    # l.visit()
    l.search(l.login_button,txt)
