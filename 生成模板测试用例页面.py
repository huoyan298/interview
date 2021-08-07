# -*- coding: utf-8 -*-
# @Time    : 
# @Author  :
# @Site    : 
# @File    : 
# @Software: PyCharm
from string import Template

# 构造单个测试集
def singleTestsuitCreate(MethodList, parameters):
    code = Template( '''suite.addTest(${className}("test_${testcase}"))''' )
    string = code.substitute( testcase=MethodList["testcase"], className=parameters[0] )
    return string

# 添加测试集
def addtestsuit(MethodParaList, interfaceNamePara):
    string = ""
    for MethodPara in MethodParaList:
        string2 = singleTestsuitCreate( MethodPara, interfaceNamePara )
        string = string + string2
    return string

# 然后测试用例部分如下：
parameters = ["Testcase_test",
              "/login",
              [
                  {"TestcaseName": "测试登录", "method": "post", "url": "http://www.baidu.com/",
                   "headers": {'content-type': 'application/json',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                               'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
                               'Accept-Language': 'zh-CN'}, "data": {"uname": "187071484771", "pwd": "123456"},
                   "testcase": "login"},

                  {"TestcaseName": "测试登录", "method": "post", "url": "http://www.senbaba.cn/login1",
                   "headers": {'content-type': 'application/json',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                               'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
                               'Accept-Language': 'zh-CN'}, "data": {"uname": "187071484771", "pwd": "123457"},
                   "testcase": "login_failed"}
              ]
              ]

def methodCreate(MethodParaList, interfaceNamePara):
    string = ""
    for MethodPara in MethodParaList:
        string2 = singleMethodCreate( MethodPara, interfaceNamePara )
        string = string + string2
    return string

# 动态生成单个测试用例函数字符串
def singleMethodCreate(MethodList, interfaceNamePara):
    code = Template( '''\n    def test_${testcase}(self):
        u"""${testcaseName}"""
        headers = $headers
        data = $data
        re = requests.$method(url='$url',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        logging.info('-'*5+'返回结果集是'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'
''' )

    string = code.substitute( testcase=MethodList["testcase"], testcaseName=MethodList["TestcaseName"],
                              method=MethodList['method'], url=MethodList['url'], headers=MethodList['headers'],
                              data=MethodList['data'],
                              )
    return string

# 生成测试用例类函数字符串
def modelClassCreate(parameters):
    modelCode = methodCreate( parameters[2], parameters[1] )
    adtestsuit = addtestsuit( parameters[2], parameters )
    code = Template( '''#coding: utf-8
"""
功能：待执行的接口测试用例
环境：python3.6
用法：通过框架自动触发调用
"""
import unittest,requests,datetime,sys,logging,BSTestRunner,time,os
from Log import Log
class ${className}(unittest.TestCase):
    u"""待测试接口：${interfaceName}"""
    def setUp(self):
        logging.info('-'*5+"begin test"+"-"*5)
    def tearDown(self):
        logging.info('-'*5+"end test"+'-'*5)
    ${model}
if __name__ == "__main__":
    #解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    ${testsuite}
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time1=time.strftime("%H%M%S")
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #创建路径
    path='D:/teststudytestlog/'+now+"/"
    #解决多次执行时报路径已存在的错误
    try:
        os.makedirs(path)
    except:
        if path!= None:
            logging.error(u'当前路径已经存在')
    filename=path+'Report.html'
    # 2021-08
    # fp=file(filename,'wb')
    with open(filename,'w',encoding='utf-8') as fp:
     #日志记录
     Log.log()
     #执行测试
     runner =BSTestRunner.BSTestRunner(stream=fp,title=u'下单平台接口测试用例',description=u'接口用例列表：')
     runner.run(suite)
     fp.close()
''' )
    fileStr = code.substitute( className=parameters[0], interfaceName=parameters[1], testsuite=adtestsuit,
                               model=modelCode )
    f = open( parameters[0] + ".py", 'w' )
    # print(parameters[0])
    f.write( fileStr )
    f.close()

if __name__ =="__main__":
  modelClassCreate(parameters)