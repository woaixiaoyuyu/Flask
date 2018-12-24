# from flask import Flask
import threading

# 自定义一个支持协程的threading

# 1.先实现基本的threading
# 将唯一标识号当作字典的key，从而隔离各个线程之间的数据

# 2.支持协程
# 增加协程的唯一标识，需要安装库gevent
# import threading
try:
    from greenlet import getcurrent as get_ident  # 协程
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident  # 线程


# 3.改为flask标准的面向对象的语法
class Local(object):

    def __init__(self):
        object.__setattr__(self, '__storage__', {})   # 不用self.storage = {} 来避免调用__setattr__
        object.__setattr__(self, '__ident_func__', get_ident)

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


local_values = Local()


def task(num):
    local_values.name = num
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,),name='线程%s' % i)
    th.start()


