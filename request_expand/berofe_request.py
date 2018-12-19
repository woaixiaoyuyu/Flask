# render_template是模板渲染，例如在开发flask项目中，我们会有一个templates文件夹，里面存放一些html文件，
# 这些文件会在视图函数中被渲染，此时就会用到render_template包
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '123456'

USERS = {
    1: {'name': 'xiaoyuyu', 'age': '18', 'sex': 'male'},
    2: {'name': 'isa', 'age': '21', 'sex': 'male'},
    3: {'name': 'rookie', 'age': '18', 'sex': 'female'}
}


@app.before_request
def process_request(*args,**kwargs):
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if user:
        return None
    return redirect('/login')


@app.route('/detail/<int:nid>', methods=['GET'])  # @app.route()是thedecorator是装饰器功能
def detail(nid):
    info = USERS.get(nid)
    print(nid)
    return render_template('detail.html', info=info)


@app.route('/index', methods=['GET'])
def index():
    # user = session.get('user_info')
    # if not user:
    #     url = url_for('yuyu')
    #     return redirect(url)
    return render_template('index.html', user_dict=USERS)


# endpoint用来反向生成url,yuyu是别名
@app.route('/login', methods=['GET', 'POST'], endpoint='yuyu')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'xiaoyuyu' and pwd == 'woaini':
            session['user_info'] = user
            return redirect('index')
        else:
            return render_template('login.html', error='wrong usernmae or password')


if __name__ == '__main__':
    app.run()
