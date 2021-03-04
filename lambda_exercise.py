# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
#1.
g=lambda x:x+1
print(g(1))
print(g(2))
#2.
foo=[2,18,9,22,16,17,24,8,12,27]
# print((filter(lambda x:x %3==0,foo)))
# print[x for x in foo if x % 3 ==0]
#3
f = lambda x,y,z:x+y+z
print(f(1,2,3))

L=[lambda x:x+2,lambda x:x*2,lambda x:x**2]
print("L=",L[0](1),L[1](2),L[2](3))