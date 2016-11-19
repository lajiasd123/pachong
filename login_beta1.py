import urllib
import urllib2

values = {}
values['username'] = ''
values['password'] = ''
data = urllib.urlencode(values)

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
headers = {'User-Agent': user_agent}
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)




print response.read()


