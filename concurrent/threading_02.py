# coding:utf-8
import sys
import threading
import time

#线程锁GIL
#多线程之间是共享内存的，对于公共资源需要加线程锁才可以正常使用。线程锁的概念就是该线程运行
