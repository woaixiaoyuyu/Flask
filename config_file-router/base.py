class Base(object):
    def send(self, msg):
        # NotImplementedError	尚未实现的方法
        # 用来约束，告诉别人需要实现send方法，不然就报错
        raise NotImplementedError
