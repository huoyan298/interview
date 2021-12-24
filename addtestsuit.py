# 添加测试集
# import Template
# -*- coding: utf-8 -*-
# @Time    :
# @Author  : 
# @Site    :
# @File    :
# @Software: PyCharm
from string import Template
def addtestsuit(parameters):
    string = ""
    temp = Template('''\n suite.addTest($className}("test_${testcase}"))''')
    l = len(parameters[2])
    for i in range(0,1):
         testcase1 = parameters[2][i]['testcase']
         string2 = temp.substitute(className = parameters[0],testcase=testcase1)
         string = string +string2
         print (string)
    return string
# 增加测试用例集EXCEL 读取用例
if __name__=="__main__":
    list_str = ["hello", "world",[{"testcase":"c"},"e","f"], "nihao", "ha"]
    # print(list_str[2][0]['testcase'])
    addtestsuit(list_str)
