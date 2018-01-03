# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    #创建Form_Data字典，存储上图的Form Data
    while True:
        str = input("请输入要翻译的英文：")
        if str == 'exit':
            print('退出！')
            break
        else:
            Form_Data = {}
            Form_Data['from'] = 'AUTO'
            Form_Data['to'] = 'AUTO'
            Form_Data['i'] = str
            Form_Data['client'] = 'fanyideskweb'
            Form_Data['smartresult'] = 'dict'
            Form_Data['doctype'] = 'json'
            Form_Data['salt'] = '1513373147047'
            Form_Data['version'] = '2.1'
            Form_Data['sign'] = '91e73dc2522a85c260dfe6848779b6db'
            Form_Data['keyfrom'] = 'fanyi.web'
            Form_Data['typeResult'] = 'false'
            Form_Data['action'] = 'FY_BY_CLICKBUTTON'
            #使用urlencode方法转换标准格式
            data = parse.urlencode(Form_Data).encode('utf-8')
            # print(data)
            #传递Request对象和转换完格式的数据
            response = request.urlopen(Request_URL, data)
            #读取信息并解码
            html = response.read().decode('utf-8')
            print(html)
            #使用JSON
            translate_results = json.loads(html)
            #找到翻译结果
            translate_results = translate_results['translateResult'][0][0]['tgt']
            #打印翻译信息
            print("翻译的结果是：%s" % translate_results)