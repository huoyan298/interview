# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from pom.BasePage import basepage
from pom.pageobject.LoginPage import LoginPage
import  unittest
from selenium import webdriver
from pom.pageobject.search_page import search_page
from ddt import ddt,file_data,data,unpack
from time import sleep

# test_data=(("txt","nihao"),("hello","Kitty"))
@ddt()
class TestCase(unittest.TestCase):
    #
    @data(("txt","hello"))
    # @data("hello",111)
    def test_1_login(self,value):
        # driver =webdriver.Firefox()
        # username = ''
        # password =''
        # txt='nihao'
        # lp=LoginPage(driver)
        # lp.login(username,password)
        # ip=IndexPage(driver)
        # lp.search(lp.search_world,txt)
        # print("a:",value[1])
        # sleep(3)
        # lp.click( lp.search_btn)
        # self.lp.search("hello")
        print(" test a:",value)
if __name__=="__main__":

    # t=TestCase()
    # t.test_1_login()

    unittest.main()
