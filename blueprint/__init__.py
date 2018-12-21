from flask import Flask

# static_url_path主要用于改变url的path的，静态文件放在static下面，
# 所以正常情况url是static/filename ，但是可以通过static_url_path来改变这个url
# static_folder主要是用来改变url的目录的，默认是static，可以通过这个变量来改变静态文件目录
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')

from .view.account import account
from .view.blog import blog
from .view.user import user

app.register_blueprint(account)
app.register_blueprint(blog)
app.register_blueprint(user)


# 可以统一处理before process
@app.before_request
def process_request(*args):
    print('comming1')
