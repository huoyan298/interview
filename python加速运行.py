# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
# 1.拼接使用join 而不用"+"
import string
from typing import List
def concat_string(str_list):
    str_result=""
    for i in list:
        str_result+=i
    return str_result

def concat_str(strlist):
    return " ".join(strlist)



# 2.交换值不使用中间变量
def swap():
    a=3
    b=7
    # temp=a
    # a=b
    # b=temp
    a,b=b,a


# 3.for循环比while快
def sum(n:int)->int:
    total=0
    # i=0
    # while i <n:
    #    total+=i
    #    i=i+1
    for i in n:
        total+=i

    return sum

# 4.避免全局变量
import  math
size =10000
for i in range(size):
    sum = math.sqrt(i)

def add_sqrt():
    size=1000
    for x in range(size):
        sum =math.sqrt(x)