# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import time,os
import pygame

BASE=os.path.dirname(os.path.abspath(__file__))
print("path:"+BASE)
words = input('Please input the words you want to say:')
# words ="Dear honey,Happy birthday !"
for item in words.split():
    letterlist =[]
    for y in range(12,-12,-1):
        list_x = []
        letters = ''
        for x in range(-30,30):
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters +=item[(x-y)%len(item)]
            else:
                letters +=" "
        list_x.append(letters)
        letterlist+=list_x
    print('\n'.join(letterlist))
    time.sleep(1)


# if __name__ =="__main__":
#     # print('\n'.join( [''.join( [''.join( ['Love'[(x - y) % len( 'Love' )] if ((x * 0.05) ** 2+ (y * 0.1) ** 2 - 1) ** 3 - ( x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else '  '))))

# 版本二

words = input('Please input the words you want to say:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y)%len(item)] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30)]) for y in range(12,-12,-1)]))