# 源码分析

# 1.__call__
# 第一个实例化对象Flask
'''将请求相关数据封装到RequestContext中'''
# ctx = self.request_context(environ)
#         error = None
#         try:
#             try:
'''再将对象封装到Local中（每个线程/协程独立）'''
'''使用request获取的信息'''
#                 ctx.push()
#                 response = self.full_dispatch_request()
#             except Exception as e:
#                 error = e
#                 response = self.handle_exception(e)
#             except:
#                 error = sys.exc_info()[1]
#                 raise
#             return response(environ, start_response)
#         finally:
#             if self.should_ignore_error(error):
#                 error = None
'''清除自己在Local中保存的数据'''
#             ctx.auto_pop(error)
#
#     def __call__(self, environ, start_response):
#         """The WSGI server calls the Flask application object as the
#         WSGI application. This calls :meth:`wsgi_app` which can be
#         wrapped to applying middleware."""
#         return self.wsgi_app(environ, start_response)
'''ctx = self.request_context(environ)'''
'''RequestContext'''
# 2.request_context
# 最后return RequestContext(self, environ)
# environ 包含请求相关所有数据，实例化了一个RequestContext对象
# def __init__(self, app, environ, request=None):
#     self.app = app
#     if request is None:
#         request = app.request_class(environ)
#     self.request = request
#     self.url_adapter = app.create_url_adapter(self.request)
#     self.flashes = None
#     self.session = None
# 此时request是None，调用app.request_class(environ)
# request_class = Request，调用第三个类

# 3.Request
'''ctx.push()'''
# 将RequestContext对象压入，带有environ
# 最后执行_request_ctx_stack.push(self)
# 全局变量_request_ctx_stack = LocalStack()

# 4.LocalStack
# 启动前就执行了
# def __init__(self):
#     self._local = Local()
# ctx.push()执行后会调用
# def push(self, obj):
#     """Pushes a new item to the stack"""
#     rv = getattr(self._local, 'stack', None)
#     if rv is None:
#         self._local.stack = rv = []
#     rv.append(obj)
#     return rv

# self._local.stack会调用Local中的setattr,最后压入请求相关的所有数据

# 5.Local
# 之前熟悉的'__storage__', '__ident_func__'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.__call__
    app.run()

