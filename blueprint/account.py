from flask import Blueprint, render_template, request

# url_prefix='/xiaoyuyu' 增加url前缀
# 同一个Blueprint下url全部加上前缀，很方便，不需要一个一个添加
# 没个蓝图可以定义不同的template_folder
# 模板路径自定制，静态文件路径自定制，但要注意优先级，最外层优先
# 批量操作url
# 请求扩展
account = Blueprint('account', __name__, url_prefix='/xiaoyuyu')


@account.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
