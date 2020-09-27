#coding:utf-8

import hashlib
def md5(s):
    return hashlib.md5(str(s).encode('utf-8')).hexdigest()
def main(s):
    for i in range(1,99999999): 
        if md5(i)[0:6]  == str(s):
            print(i)
            exit(0)
if __name__ == '__main__':
    main("2b8041")

"""
从1至9999999进行MD5编码
从中截取前6位与main()对比
输出i的值则为验证码Captcha的值
"""