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
@ddt
class TestCase():
    # noinspection PyUnresolvedReferences
    '''
    @classmethod
    def setUpClass(cls)->None:
       cls.driver = webdriver.Firefox()
       cls.lp = LoginPage(cls.driver)
       cls.ip = search_page(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @file_data('../data/user.yaml')
    def test_1_login(self):
        driver =webdriver.Firefox()
        # username = ''
        # password =''
        txt='衣服'
        # lp=LoginPage(driver)
        # lp.login(username,password)
        # ip=IndexPage(driver)
        # ip.search(txt)
        sleep(3)
    '''

    @data(["txt","hello"])
    @unpack
    def test_1_login(self):
        driver =webdriver.Firefox()
        # username = ''
        # password =''
        # txt='nihao'
        lp=LoginPage(driver)
        # lp.login(username,password)
        # ip=IndexPage(driver)
        lp.search(lp.search_world,"txt")
        # print(txt)
        sleep(3)
        lp.click( lp.search_btn)
        # self.lp.search("hello")

if __name__=="__main__":

    t=TestCase()
    t.test_1_login()
    # unittest.main()
