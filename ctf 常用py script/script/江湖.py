import base64
import urllib.parse

data = 'O:5:"human":10:{s:8:"xueliang";i:576;s:5:"neili";i:652;s:5:"lidao";i:77;s:6:"dingli";i:66;s:7:"waigong";i:0;s:7:"neigong";i:0;s:7:"jingyan";i:0;s:6:"yelian";i:0;s:5:"money";i:2000000;s:4:"flag";s:1:"0";}'
with open('C:\\Users\\MUMU\\Desktop\\a.bin', 'wb') as f:
    for i in range(0, len(data)):
        num = ord(data[i])
        num = num + ((i % 10) + 2)
        num = num ^ i
        f.write(bytes([num]))

d = open('C:\\Users\\MUMU\\Desktop\\a.bin', 'rb').read()[:]
a = base64.b64encode(d)
b = urllib.parse.quote(a)
print(b)