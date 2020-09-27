import hashlib

cookies_secret = "dda27ce2-042e-43d9-9ae7-aa8e432caea1"
filename="/fllllllllllllag"
file_md5=hashlib.md5(filename.encode('utf8')).hexdigest()
cookies_secret=hashlib.md5(cookies_secret.encode('utf8')).hexdigest()
sss=(file_md5+cookies_secret).encode('utf8')
final_md5 = hashlib.md5(sss)
print(final_md5)