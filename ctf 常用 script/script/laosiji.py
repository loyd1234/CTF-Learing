import re
import requests
url = 'http://183.60.253.188:8083/ctf/9l82aXzNQ7AaAmvC/index.php?rnd=9de7246aaa0ab0f31kjil5j4'
s = requests.Session()
source = s.get(url)
expression = re.search(r'(\d+[+\-*])+(\d+)', source.text).group()
result = eval(expression)
post = {'value': result}
em = s.post(url, data = post).text

    