# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 私钥解密
# @Software: PyCharm
# b'CNBr9kbb2QoOZ0F1Pp/GgPVRSb+5mBplYmHf1X59Ej8SN0mLYMxw/qmcUeATHWNGZEwkLfoXRDSn7759cxQcAiVqo66LScQSYLPg6ub2fgrwukocb7w5wT7UQ9younxGJ6v3brQ6sXH8J2UwTj60dc2WDDykBhBWRTvoZfDi1Ng='


import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
# 密文
# msg=b'TFxtcoqvYJCR65uy9TTMl0zGbU3WXF7gWkkFrCsR6YCkx9pX9ww7UX6taTzLWy/PatqA+LYkq6vbyd3IjT6bQvOcx/qnIE/JmixWwaIeDB7+f7Dzdbfpu06NBkD5Mv4LjDaT8ptwloXDe0sLZgi00v5GE//KVShK0y7+fpB/wVQ='

# base64解码
msg = base64.b64decode(b'TFxtcoqvYJCR65uy9TTMl0zGbU3WXF7gWkkFrCsR6YCkx9pX9ww7UX6taTzLWy/PatqA+LYkq6vbyd3IjT6bQvOcx/qnIE/JmixWwaIeDB7+f7Dzdbfpu06NBkD5Mv4LjDaT8ptwloXDe0sLZgi00v5GE//KVShK0y7+fpB/wVQ=')
# 获取私钥
privatekey = open('private.pem').read()
rsakey = RSA.importKey(privatekey)
# 进行解密
cipher = PKCS1_v1_5.new(rsakey)
# text = cipher.decrypt(msg)
text = cipher.decrypt(msg, 'DecryptError')
# 解密出来的是字节码格式，decodee转换为字符串
print(text)
print(text.decode())