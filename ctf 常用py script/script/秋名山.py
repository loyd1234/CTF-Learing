#!/usr/bin/python
#coding:utf-8
import requests
import re
url = 'http://183.60.253.188:8083/ctf/9l82aXzNQ7AaAmvC/index.php?rnd=9de7246aaa0ab0f31kjil5j4'  # 这个URL是不定的
s = requests.session()
g = s.get(url)
page = re.findall(r'<div id=\'calc\'>(.*)=\?;</div>', g.text)
# print(page[0])
page1 = page[0].replace('X','*')
res = eval(page1)
payload = {'value': res}
p = s.post(url, data=payload)
print p.text