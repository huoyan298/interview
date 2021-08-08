# -*- coding: utf-8 -*-
# @Time    : 
# @Author  :
# @Site    : 
# @File    : 
# @Software: PyCharm
"""
1.增加控制台打印开关

解析用例管理表，生成测试脚本框架

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# !python3__author__ = "xxx""""自动化脚本生成工具"""
import os
import xlrd, time
TestCaseName = ""
TestCaseDescription = ""
TestCasePreCondition = ""
TestCaseStep = ""
TestCaseExpectResult = ""
TestEnvironment = ""
TestScriptName = ""
cur_path = os.getcwd()
OPEN_PRINT = False
def scripts_template():
    testcases = os.path.join(cur_path, u"用例模板.xlsx")
    data = xlrd.open_workbook(r'%s' % testcases)
    table = data.sheet_by_index(0)
    n_rows = table.nrows
    n_cols = table.ncols
    if OPEN_PRINT ==True:
     print(table.name,n_rows,n_cols)
    for i in range(1, n_rows):
        TestCaseName = table.cell_value(i, 1)
        TestCaseDescription = table.cell_value(i, 2)
        TestCasePreCondition = table.cell_value(i, 3)
        TestCaseStep = table.cell_value(i, 4)
        TestCaseExpectResult = table.cell_value(i, 5)
        TestEnvironment = table.cell_value(i, 0)
        TestScriptName = "test_{0}".format(TestCaseName)
        #符合unittest测试用例定义的识别条件， 以"test"开头
        filename = os.path.join(cur_path, "{0}.py".format(TestScriptName))
        if OPEN_PRINT == True:
         print( "filename:", filename )
        with open(filename, 'w', encoding='utf-8') as out:
            out.write('''# !/usr/bin/env python
            
# -*- coding:utf-8 -*-
"""
#-----------------------------------------------------------------------
用例名称: {0}
用例描述: {1}
前置条件:
{2}
测试步骤:
{3}
预期结果:
{4}
测试环境: {5}
作者：{6}
日期：{7}
#-----------------------------------------------------------------------
"""
import unittest
class {8}(unittest.TestCase):
    def setUp(self):
        #TODO 添加用例执行前置条件
        pass
    def testRun(self):
        #TODO 添加用例执行测试步骤
        pass
    def tearDown(self):
        #TODO 添加恢复测试环境操作
        pass
        
if __name__ == '__main__':
    unittest.main()'''.format( TestCaseName, TestCaseDescription, TestCasePreCondition, TestCaseStep, TestCaseExpectResult, TestEnvironment,(TestCaseDescription), time.strftime( '%Y-%m-%d' ), TestScriptName ) )
    if OPEN_PRINT == True:
       print("generate scripts finished!")

if __name__ == "__main__":
  if OPEN_PRINT == True:
    print("case_01_01_01_01")
  scripts_template()


"""
# 运行一下以上测试脚本生成代码。生成的脚本如下：
1  # !/usr/bin/env python 2 # -*- coding:utf-8 -*- #-----------------------------------------------------------------------
6 用例名称: case_01_01_01_01 
7 用例描述: 测试天气提示刷新 
8 前置条件: 
9 打开天气APP
10 测试步骤:
11 1.后台设置今日天气为多云，查看App提示是否更新。
12 预期结果:
13 页面天气提示刷新为多云
14 测试环境: Phone15 作者：xxx16 日期：2019-01-0817 #-----------------------------------------------------------------------18 import unittest
class test_case_01_01_01_01(unittest.TestCase):     
    def setUp(self):      
    #TODO 添加用例执行前置条件      
      pass    
    def testRun(self):
     #TODO 添加用例执行测试步骤       
       pass    
     def tearDown(self):         
     #TODO 添加恢复测试环境操作         
       pass
if __name__ == '__main__':    
    unittest.main()
"""