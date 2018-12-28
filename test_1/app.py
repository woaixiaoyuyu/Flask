from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['DEBUG'] = 1
app.config['SECRET_KEY'] = '123445'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


# @app.route('/', methods=['GET', 'POST'])
# def hello():
#     form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         return redirect(url_for('hello'))
#     return render_template('index.html', form=form, name=session.get('name'))


@app.route('/', methods=['GET', 'POST'])
def main():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Look like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('main'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/time')
def time():
    return render_template('time.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def index(name):
    # app.app_context().push()
    # print(current_app.name)
    # app.app_context().pop()
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_bot_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

