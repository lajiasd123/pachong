import urllib2
import urllib
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.zhihu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

