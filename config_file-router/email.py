from .base import Base


class Email(Base):
    # 邮箱发送提醒
    def __init__(self):
        self.username = 'lalala'
        self.pwd = '123456'

    def send(self, msg):
        pass
