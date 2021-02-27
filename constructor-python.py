# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import time
import random
class Date:
  # 主构造函数
  def __init__(self,year,month,day):
      self.year =year
      self.month = month
      self.day = day

  #可选构造函数
  @classmethod
  def today(cls):
      t=time.localtime()
      return cls(t.tm_year,t.tm_mon,t.tm_mday)


a=Date(2012,12,21)
print(a.year,a.month,a.day)

b=Date.today()
print(b.year,b.month,b.day)

def random_holes():
    b=random.random()
    return b

class Cheese():
    def __init__(self,*args,**kwargs):
        self.num_holes = kwargs.get('num_holes',random_holes())


    def log_print(self):
        print(self.num_holes)

c=Cheese()
c.log_print()