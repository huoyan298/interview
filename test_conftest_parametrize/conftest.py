# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import pytest
from filelock import FileLock
@pytest.fixture(scope="session")
def login():
    print("test51job:====登录功能，返回账号，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name,token
    print("test51job:===退出登录！！！====")
