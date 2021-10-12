# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
try:
   fp = open('test.txt','r')
   for line in fp.readlines():
    print(line)
except OSError:
   raise
# print(fp.encoding)
finally:
    fp.close()


# 二
with open('test.txt','r') as file:
    for line in file.readlines():
        print(line)