# -*- coding: utf-8 -*-
from PIL import Image
 
savepath='C:\\Users\\MUMU\\Desktop\\hld\\'
im=Image.open('C:\\Users\\MUMU\\Desktop\\Traffic_Light.gif')
try:
#tell是帧数，而seek是取当前帧数的图片。
  im.save(savepath+'light{0}.png'.format(im.tell()))
  while True:
    im.seek(im.tell()+1)
    im.save(savepath+'light{0}.png'.format(im.tell()))
except:
  pass
 
flag=""
for i in range(1168):
  image=Image.open(savepath+'light'+str(i)+'.png')
  #print image.getpixel((115,55))#输出颜色值
  #print image.getpixel((115,145))
  if image.getpixel((115,55))==251:
    flag+=str(1)
  elif image.getpixel((115,145))==186:
    flag+=str(0)
flag= hex(int(flag,2))[2:-1].decode('hex')#二进制转字符串
print flag
 