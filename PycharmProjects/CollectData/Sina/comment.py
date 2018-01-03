import requests
import json
import re

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&' \
             'channel=sh&newsid=comos-{}&group=undefined&compress=0' \
             '&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&' \
             'h_size=3&thread=1'
def GetID(newsurl):
    newid = newsurl.split('/')[-1].rstrip('shtml').lstrip('doc-i')
    return newid

def GetCommentCount(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newid = m.group(1)
    comments = requests.get(commentURL.format(newid))
    comments.encoding = 'utf-8'
    jd = json.loads(comments.text)
    commentsnum = jd['result']['count']['total']
    return commentsnum


