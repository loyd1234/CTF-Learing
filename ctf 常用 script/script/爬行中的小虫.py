#!/usr/bin/python
#coding:utf-8
import requests
import base64

url = 'http://123.206.31.85:10013/index.php' 
s = requests.session()
g = s.get(url)
flag = base64.b64decode(g.headers["Password"])
data = {
    "password":flag[5:-1],
}

print s.post(url,data=data).content