import re
import pyperclip
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

neirong = str(pyperclip.paste())
tupian_tiaojian = re.compile('http://[^\s]+.jpg')
tupian_url = tupian_tiaojian.findall(neirong)
shuchu = []
for i in tupian_url:
    shuchu.append(i)
print shuchu



