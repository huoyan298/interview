# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import requests,json

url="https://www.baidu.com"
# 请求头
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

# 发起请求
response = requests.get(url,headers=headers)
# 响应状态码
response.status_code
# 响应文本
response.text
# 响应内容
response.content
# 响应头
response.headers

print("text"+response.text)
print("content"+json.dumps(dict(response.headers)))
print("header"+str(response.status_code))