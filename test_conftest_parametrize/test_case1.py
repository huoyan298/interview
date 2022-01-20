# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import pytest
from time import sleep
@pytest.mark.parametrize("n",list(range(5)))
def test_get_info(login,n):
    sleep(1)
    name,token = login
    print("test_case:****基础用例，获取用户个人信息***",n)
    print(f"test_case:用户名：{name},token:{token}")