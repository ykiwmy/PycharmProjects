# -*- coding=utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import time


num = 1  #用来计数，计算爬取的书一共有多少本
start_time = time.time()  #计算爬虫爬取过程时间

# 第一页网页网址https://read.douban.com/columns/category/all?sort=hot&start=0
# 第二页网页网址https://read.douban.com/columns/category/all?sort=hot&start=10
# 第三页网页网址https://read.douban.com/columns/category/all?sort=hot&start=20
# ......发现规律了吗
url = 'https://read.douban.com/columns/category/all?sort=hot&start='


for i in range(0,1650,10):  #这里的  range（初始，结束，间隔）
    #urllib.request库用来向该网服务器发送请求，请求打开该网址链接
    html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
    #BeautifulSoup库解析获得的网页，第二个参数一定记住要写上‘lxml’，记住就行
    bsObj = BeautifulSoup(html, 'lxml')

    print('==============' + '第%d页'%(i/10 + 1) + '==============')
    #分析网页发现，每页有10本书，而<h4>标签正好只有10个。
    h4_node_list = bsObj.find_all('h4')  # 这里返回的是h4标签的list列表
    for h4_node in h4_node_list:  #遍历列表
        #获取h4标签内的a标签，但这里返回是只含1个元素的list
        a_node = h4_node.contents[0]
        title = a_node.contents[0]  #因为是列表，要list[0]，取出来
        title = '<<' + title + '>>'
        print('第%d本书'%num, title)
        num = num + 1
    # 设置抓数据停顿时间为1秒，防止过于频繁访问该网站，被封
    time.sleep(1)


end_time = time.time()
duration_time = end_time - start_time
print('运行时间共：%.2f'  % duration_time + '秒')
print('共抓到%d本书名'%num)

