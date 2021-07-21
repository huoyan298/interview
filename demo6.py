# -*- coding: utf-8 -*-
# @Time    : 
# @Author  :
# @Site    : 
# @File    : 
# @Software: PyCharm
import requests
from tqdm import tqdm

def download(url:str,file_name:str):
    """
    根据文件直接和文件名下载文件
    :param url:
    :param file_name:
    :return:
    """
    # 文件下载直链
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    # 发起head请求，即只会获取响应头部信息
    head =requests.head(url,headers=headers)
    file_size = head.headers.get('Content-Length')
    if file_size is not None:
        file_size = int(file_size)
    response = requests.get(url,headers=headers,stream=True)
    #
    chunk_size = 1024
    bar = tqdm(total=file_size,desc=f'下载文件 {file_name}')
    with open(file_name,mode='wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
    bar.close()

if "__main__" == __name__:
    url = 'https://onlinedown.rbread04.cn/huajunsafe/dyfxrhdfafw.zip'
    file_name = 'dyfxrhdfafw.zip'
    download(url, file_name)