# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import requests
import json

def login():
    url="http://xxx.xxxx.com/xxx/login"
    headers ={'content-Type':'application/json;charset=UTF-8'}
    request_type ={ "phone":"159xxxxxxxx","password":"11111"},
    response =requests.post(url,data=json.dumps(request_type),headers = headers)
    return response.json()["object"]["token"],response.text

