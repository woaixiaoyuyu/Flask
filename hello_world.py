from flask import Flask

app = Flask(__name__)


@app.route('/')  # @app.route()是thedecorator是装饰hello_world()功能
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
