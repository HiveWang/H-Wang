# coding:utf-8
import sys
import threading
import time

#多线程编程：核心用法
# mainthread线程启动一个线程来执行函数，并自定义自线程名字：小李

def loop():
    #定义一个循环函数，然后后面定义其他函数
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 10:
        n = n + 1
        print('%s >>> %s' % (threading.current_thread().name, n))
    print('thread %s is running...' % threading.current_thread().name)

#祝线程threading_01.py
print('thread %s is running' % threading.current_thread().name)

t = threading.Thread(target=loop,name='小李')
t.start()
t.join()
print("ending...%s" % threading.current_thread().name)