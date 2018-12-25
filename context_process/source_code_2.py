from flask import Flask, request

app = Flask(__name__)


# 查看request的来历
# 全局变量
# request = LocalProxy(partial(_lookup_req_object, 'request'))
# partial 偏函数，对象是_lookup_req_object函数，附带一个request参数

# LocalProxy（函数）
# def _lookup_req_object(name):
#     top = _request_ctx_stack.top
#     if top is None:
#         raise RuntimeError(_request_ctx_err_msg)
#     return getattr(top, name)

# .top
# def top(self):
#     """The topmost item on the stack.  If the stack is empty,
#     `None` is returned.
#     """
#     try:
#         return self._local.stack[-1]
#     except (AttributeError, IndexError):
#         return None
# 取出索引为-1的值，返回一个RequestContext对象

# getattr(top, name)
# 从对象中取出name的值，即'request'的值
@app.route('/')
def hello_world():
    print(request.method)
    return 'Hello World!'


if __name__ == '__main__':
    app.request_class
    app.run()
