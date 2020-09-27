import requests
import re
so = requests.Session()
vl = 'ea'
url1 = 'http://051becfbf82a4c88952fddd4b46e264b8840ad29c3c74315.changame.ichunqiu.com/?value[]=%s'%vl

for i in range(0,30):
    html1 = requests.get(url1)
    s = html1.text
    o = s[0:2]
    url2 = 'http://051becfbf82a4c88952fddd4b46e264b8840ad29c3c74315.changame.ichunqiu.com/?value[]=%s'%o
    html2 = so.get(url2)
    sss = html2.text
    pattern = re.compile(r'flag{*')
    a = re.match(pattern, sss)
    print(a)
