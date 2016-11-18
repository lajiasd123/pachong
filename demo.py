import urllib2

website = raw_input("please input a website\n"">>>")
request = urllib2.Request(website)
response = urllib2.urlopen("http://" + website)

print response.read()
