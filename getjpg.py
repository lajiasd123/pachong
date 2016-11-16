#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# http://img1.gamersky.com/image2016/11/20161110_zq_281_8/gamersky_01small_02_201611102224426.jpg
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x += 1




html = getHtml("http://pic.gamersky.com/html/774859.shtml")

print getImg(html)
