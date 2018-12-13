# render_template是模板渲染，例如在开发flask项目中，我们会有一个templates文件夹，里面存放一些html文件，
# 这些文件会在视图函数中被渲染，此时就会用到render_template包
from flask import Flask, render_template, request, redirect
 
app = Flask(__name__)
 
 
@app.route('/login', methods=['GET', 'POST'])  # @app.route()是thedecorator是装饰器功能
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'xiaoyuyu' and pwd == 'woaini':
            return redirect('https://blog.csdn.net/qq_42192672')
        else:
            return render_template('login.html', error='wrong usernmae or password')
 
 
if __name__ == '__main__':
    app.run()
