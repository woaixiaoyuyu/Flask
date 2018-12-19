from .base import Base
# 加载当前目录下base.py下的子模块Base


class Msg(Base):
    # 短信发送提醒
    def __init__(self):
        self.username = 'lalala'
        self.pwd = '123456'

    def send(self, msg):
        pass
