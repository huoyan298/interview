# -*- coding: utf-8 -*-
# @Time    : 
# @Author  :
# @Site    : 
# @File    : 
# @Software: PyCharm

# 导入requests库
import requests
# 自己找个资源测试下载

url='https://onlinedown.rbread04.cn/huajunsafe/dyfxrhdfafw.zip'

file_name ='dyfxrhdfafw.zip'
# 请求头
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
print('正在下载文件......')
# 发起请求
response = requests.request('get',url,headers=headers)
content = response.content
# 以wb的模式打开文件
with open(file_name,mode='wb') as f:
     f.write(content)
print(f'文件下载成功!文件名 {file_name}')