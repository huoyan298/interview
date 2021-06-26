# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import  requests
url='https://onlinedown.rbread04.cn/huajunsafe/dyfxrhdfafw.zip'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
# 发起head请求，即只会获取响应头信息
response = requests.head(url,headers=headers)
# 文件大小，以B为单位
file_size = response.headers.get('Content-Length')
if  file_size is not None:
    file_size = int(file_size)
print('文件大小:',file_size,'B')
