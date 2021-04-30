# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import json
from pprint import pprint
# 反斜杠 D:\test\db.json
with open('D:/test/db.json') as j:
    cfg=json.load(j)['localdb']
pprint(cfg)

# ini
from configparser import  ConfigParser
cfg = ConfigParser()
cfg.read("D:/test/ini.ini")
cfg.items("localdb")
pprint(cfg.items("localdb"))
pprint(cfg["localdb"]["host"])

#toml



# yaml
import  os
from pprint import pprint
import  yaml
# yaml 冒号后面需要空格，
with open(os.path.expanduser("D:/test/config.yaml"),"r") as config:
      cfg= yaml.safe_load(config)

pprint(cfg)


# 