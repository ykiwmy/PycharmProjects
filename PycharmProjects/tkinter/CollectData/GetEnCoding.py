# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")

    print("geturl打印信息：%s" % (response.geturl())) # geturl()返回的是一个url的字符串；
    print('**********************************************')
    print("info打印信息：%s" % (response.info()))  # info()返回的是一些meta标记的元信息，包括一些服务器的信息；
    print('**********************************************')
    print("getcode打印信息：%s" % (response.getcode()))  # getcode()返回的是HTTP的状态码，如果返回200表示请求成功。

    html = response.read()
    charset = chardet.detect(html)
    print(charset)
