import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import pandas
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time, h2, a)

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&' \
             'channel=sh&newsid=comos-{}&group=undefined&compress=0' \
             '&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&' \
             'h_size=3&thread=1'
def GetCommentCount(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newid = m.group(1)
    comments = requests.get(commentURL.format(newid))
    comments.encoding = 'utf-8'
    jd = json.loads(comments.text)
    commentsnum = jd['result']['count']['total']
    return commentsnum


def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    timesource = soup.select('.date')[0].text
    result['dt'] = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
    result['source'] = soup.select('.source')[0].text
    result['article'] = ''.join(p.text.strip() for p in soup.select('.article p')[:-1])
    result['editor'] = soup.select('.show_author')[0].text.strip('责任编辑：')
    result['Comments'] = GetCommentCount(newsurl)
    return result
print(1)
print(getNewsDetail('http://news.sina.com.cn/c/nd/2017-12-24/doc-ifypyuva7207384.shtml'))
url = 'http://api.roll.news.sina.com.cn/zt_list?' \
      'channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&' \
      'level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&' \
      'page={}'

def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

news_total = []
for i in range(1, 3):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)

df = pandas.DataFrame(news_total)
#df.to_excel('sina.xlsx')
