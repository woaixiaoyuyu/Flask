from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], endpoint='yuyu')  # @app.route()是thedecorator是装饰器功能
# 关键就是执行self.add_url_rule(rule, endpoint, f, **options)
# app.add_url_rule('/', 'yuyu', index, methods=['GET', 'POST'])
# return index
# tips:
#    if no endpoint:
#        endpoint = 函数名，如下即index
def index():
    return 'Hello World!'
# 引出第二种@app.route的方法，直接添加进路由表：
# def index():
#     return 'Hello World!
# app.app.add_url_rule('/', 'yuyu', index, methods=['GET', 'POST'])
# Flask路由添加是通过装饰器，但本质就是添加路由 self.add_url_rule


if __name__ == '__main__':
    app.run()
