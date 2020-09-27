import re
import requests
import time

url = 'http://8e023c5a6336fedd.synctf.com:8002/coding/code08/'

res = requests.session()

ans1 = res.get(url)
# print ans1.content
calc = re.findall(r">(.*?)</div>",ans1.content)
s = "".join(calc).strip('=')
ans = eval(s)
while True:
    try:
        print '[+]Attacked by 0verWatch'
        time.sleep(1)
        ans2 = res.post(url=url,data={"ans":ans}).content
        calc = re.findall(r">(.*?)</div>",ans2)
        s = "".join(calc).strip('=')
        ans = eval(s)
    except:
        print ans2
        break