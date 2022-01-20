# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from time import sleep
import  pytest
@pytest.mark.parametrize("n",list(range(5)))
def test_no_fixture(login,n):
    sleep(1)
    print("=test_case2:test_no_fixture:没有__init__测试用例")