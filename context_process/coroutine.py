from _thread import get_ident   # 获取线程的唯一标识
# from flask import Flask
import threading
from greenlet import getcurrent as get_ident

# 自定义一个支持协程的threading

# 1.先实现基本的threading
# 将唯一标识号当作字典的key，从而隔离各个线程之间的数据

# 2.支持协程
# 增加协程的唯一标识，需要安装库gevent
# import threading
# try:
#     from greenlet import getcurrent as get_ident # 协程
# except ImportError:
#     try:
#         from thread import get_ident
#     except ImportError:
#         from _thread import get_ident # 线程


class Local(object):
    def __init__(self):
        self.storage = {}
        self.get_ident = get_ident()

    def set(self, k, v):
        ident = get_ident
        orgin = self.storage.get(ident)
        if not orgin:
            orgin = {k: v}
        else:
            orgin[k] = v
        self.storage[ident] = orgin

    def get(self, k):
        ident = get_ident
        orgin = self.storage.get(ident)
        if not orgin:
            return None
        return orgin.get(k, None)


local_values = Local()


def task(num):
    local_values.set('name', num)
    import time
    time.sleep(1)
    print(local_values.get('name'), threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,), name='thread %s' % i)
    th.start()

# app = Flask(__name__)
#
#
# # @app.route('/')
# # def hello_world():
# #     return 'Hello World!'
# #
# #
# # if __name__ == '__main__':
# #     app.run()
