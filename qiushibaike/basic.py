# -*- coding:UTF-8 -*-
import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
headers = {'User-Agent':user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?"content">.*?<span>(.*?)</span>.*?</div>.*?number">(.*?)</.*?number">(.*?)</.',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1],item[2],item[3]

#    print response.read()
except urllib2.URLError, e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason

