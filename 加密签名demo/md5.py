# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : Reference code
# @Software: PyCharm
from Crypto import Random
from Crypto.PublicKey import  RSA
# 开始还以为这个 .read 是个方法，却带参数；多方查找验证，应该是个属性值
random_str = Random.new().read
rsa_str = RSA.generate(1024,random_str)
# 获取私钥，保存文件
private_mima  = rsa_str.exportKey()
with open('private.pem','wb') as f:
    f.write(private_mima)


# 获取公钥保存到文件
public_mima = rsa_str.publickey().exportKey()
with open('public.pem','wb') as f:
    f.write(public_mima)
