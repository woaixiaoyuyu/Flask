# Request.Form：获取以POST方式提交的数据（接收Form提交来的数据）；
# Request.QueryString：获取地址栏参数(以GET方式提交的数据)
# Request：包含以上两种方式(优先获取GET方式提交的数据)，它会在QueryString、Form、ServerVariable中都搜寻一遍。
from flask import Flask, flash, get_flashed_messages, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xiaoyuyu'


@app.route('/index')
def index():
    # request.form.get("key", type=str, default=None) 获取表单数据
    # request.args.get("key") 获取get请求参数
    # request.values.get("key") 获取所有参数
    val = request.args.get('v')
    if val == 'xiaoyuyu':
        return 'Hello world!'
    # flash防止恶意代码，构建恶意url，阅后即焚，本质类似于session.pop
    flash('Error1', category='ERROR')  # 把错误信息放在ERROR分类中，方便获取
    return redirect('/error')


@app.route('/error')
def error():
    # 从某个地方获取设置的值，并清除
    data = get_flashed_messages(category_filter=['ERROR'])
    # print(type(data))
    msg = data[0]
    return 'ERROR: %s' % (msg,)


if __name__ == '__main__':
    app.run()
