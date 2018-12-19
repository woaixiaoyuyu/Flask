import settings
import importlib


def send_msgs(msg):
    for path in settings.MSG_List:
        # S.rsplit([sep=None][,count=S.count(sep)])
        # sep -- 可选参数，指定的分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        # count -- 可选参数，分割次数，默认为分隔符在字符串中出现的总次数
        m, c = path.rsplit('.', maxsplit=1)
        # m=utils.Message.email/msg
        # c=Email/Msg
        md = importlib.import_module(m)  # 动态导入模块
        obj = getattr(md, c)()  # 实例化一个对象
        obj.send(msg)
