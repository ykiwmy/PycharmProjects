import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime



res = requests.get('http://news.sina.com.cn/c/nd/2017-12-24/doc-ifypyuva7207384.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select('.main-title')[0].text
print(title)
#字串转时间--strptime
#时间转字串--strftime
timesource = soup.select('.date')[0].text
dt = datetime.strptime(timesource,'%Y年%m月%d日 %H:%M')
print(dt)

source = soup.select('.source')[0].text
print(source)

article = []
for p in soup.select('.article p')[:-1]:
    article.append(p.text.strip())
print(' '.join(article))

editor = soup.select('.show_author')[0].text.strip('责任编辑：')
print(editor)

commentnum  = soup.select('.num')[0].text
print(commentnum)

