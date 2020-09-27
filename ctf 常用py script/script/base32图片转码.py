import base64
l1 = []
with open('jpg_pic.jpg', 'rb') as f:
    b32 = f.readlines()
#print b32
    b32=''.join(b32)
with open('jpg3.jpg', 'wb') as f:
    f.write(base64.b32decode(b32))

print 'done'