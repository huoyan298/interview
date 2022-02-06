# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from selenium.webdriver.common.by import By

from pom.BasePage.basepage import basepage
from selenium import webdriver


class search_page(basepage):
    url='https://www.baidu.com/'
    search_btn=(By.XPATH,'//*[@id="su"]')
    search_wd =  (By.XPATH,'//*[@id="kw"]')
    # txt="nihao"
    def search(self,search_By,txt):
        self.visit()
        self.input_txt(self.search_wd,txt)
        self.click(self.search_btn)


if __name__=="__main__":
    driver =webdriver.Firefox()
    s=search_page(driver)
    s.search(s.search_wd,"kitty")