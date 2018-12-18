from flask import Flask, render_template, Markup

app = Flask(__name__)


# 传递函数
def func1():
    return "xiaoyuyu"


# 传递html字段
def func2(argv):
    return "<input type='text' value='%s' />" % (argv,)  # 防止最基础的XSS的好方法


# Markup函数对字符串进行转移处理再传递给render_template()函数,和前端的safe作用相同
def func3(argv):
    return Markup("<input type='text' value='%s' />" % (argv,))


@app.route('/')  # @app.route()是thedecorator是装饰hello_world()功能
def index():
    return render_template("Jinja2_1.html", index=func1, index2=func2, index3=func3)


if __name__ == '__main__':
    app.run()
