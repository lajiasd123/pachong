import cookielib
import urllib2

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True, ignore_discard=True)
req = urllib2.Request('http://www.qiushibaike.com/')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()