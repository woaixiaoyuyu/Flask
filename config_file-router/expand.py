from flask import Flask, request
from utils.message import send_msgs

app = Flask(__name__)


@app.route('/')
def index():
    data = request.query_string('val')
    if data == 'alert':
        # 发送警报：短信/邮件
        send_msgs('...')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
