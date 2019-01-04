from flask import Flask, request, render_template, url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from threading import Thread
import os
import pymysql

app = Flask(__name__)

# os.path.abspath(path)	返回绝对路径
# os.path.dirname(path)	返回文件路径/目录路径
# basedir = os.path.abspath(os.path.dirname(__file__))

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hard to guess string'

# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xiaoyuyu@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MALT_PORT'] = 465  # 465 or 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '**********@qq.com'
app.config['MAIL_PASSWORD'] = '************'
app.config['FLASKY_ADMIN'] = '*********@qq.com'  # this is the email of admin
app.config['FLASKY_MAIL_SENDER'] = '*********@qq.com'  # this is sender
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'  # 只是在主题前面加个修饰前缀

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)


# 发邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


class Role(db.Model):
    __tablename__ = 'roles'
    users = db.relationship('User', backref='role')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # 返回一个可以用来表示对象的可打印字符串
    # %r用repr()方法处理对象
    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


class NameFrom(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
# @app.route('/')
# def index():
#     # request 请求上下文，封装了客户端发出的HTTP请求中的内容
#     user_agent = request.headers.get('User-Agent')  # 同一线程下的全局变量
#     return '<p>Your browser is {}</p>'.format(user_agent)


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

# @app.route('/')
# def index():
#     return render_template('index.html', current_time=datetime.utcnow())
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


# db.drop_all()
# db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        # 如果没有用户
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_mail(app.config['FLASKY_ADMIN'], 'New User', 'new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
