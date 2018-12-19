# 好的应用和用户界面的重点是回馈。如果用户没有得到足够的反馈，他们可能最终会对您的应用产生不好的评价。
# Flask 提供了一个非常简单的方法来使用闪现系统向用户反馈信息。
# 闪现系统使得在一个请求结束的时候记录一个信息，然后在且仅仅在下一个请求中访问这个数据。
# 这通常配合一个布局模板实现
# flash主要用与对临时数据的操作，如错误信息

from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xiaoyuyu'


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/get')
def get():
    # 从某个地方获取设置的值，并清除
    data = get_flashed_messages()
    # print(type(data))
    print(data)
    return 'Hello World!'


@app.route('/set')
def set():
    # 设置一个值
    flash('xiaoyuyu')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
