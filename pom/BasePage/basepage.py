# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from selenium import  webdriver
from time import sleep


class basepage(object):
    # driver = webdriver.Firefox()
    def __init__(self,driver):
        self.driver=driver

    # def visit(self,url):
    #     self.driver.get(url)

    def visit(self):
        print("basepage+visit")
        self.driver.get(self.url)

    def locator(self,loc):
        return self.driver.find_element(*loc)


    def input_txt(self,loc,txt):
        print("basepage+input_txt")
        return self.locator(loc).send_keys(txt)

    def click(self,loc):
        self.locator(loc).click()

    def wait(self,time_):
        sleep(time_)

    # def quit_(self,loc):

if __name__=="__main__":
   driver = webdriver.Firefox()
   b=basepage(driver)
   url="http://www.baidu.com"
   # b.visit(url)