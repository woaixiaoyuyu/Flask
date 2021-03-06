from flask import Flask

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'], endpoint='yuyu')  # @app.route()是thedecorator是装饰器功能
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

# 重定向 redirect_to，如下查询index2时会自动跳转到index
@app.route('/index2', methods=['GET', 'POST'], endpoint='yuyuyuyu', redirect_to='index')
def index2():
    return 'Hello World!'

# 常用路由系统有以下五种
'''
@app.route('/user/<username>') 字符串
@app.route('/post/<int:post_id>') 整数
@app.route('/post/<float:post_id>') 小数
@app.route('/post/<path:path>') 路径
@app.route('/login', methods=['GET', 'POST'])
'''

if __name__ == '__main__':
    app.run()
