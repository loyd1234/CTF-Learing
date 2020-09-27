#-*- coding:UTF-8 -*-
import re
import requests
#var = 1 #无限循环
while True:
    url = 'http://123.206.31.85:10020/'
    s = requests.Session()
    source = s.get(url).text
    expression = re.findall(r'[0-9a-z]{33}'+'<br/>',source)[0]#先将<br/>前面34位数字提取出来
    ss = re.findall(r'[0-9a-z]{33}',expression)[0]#去掉<br/>
    url2 = url+'?key='+ss
    text2= s.get(url2).text.encode("gbk", "ignore")
    print text2
        
# 多跑几遍