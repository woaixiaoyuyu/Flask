from flask import Flask

app = Flask(__name__)
# 接下来选择配置文件来代替所有的app.config
app.config.from_object('S3_settings.DevelopmentConfig')


@app.route('/')  # @app.route()是thedecorator是装饰器功能
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
