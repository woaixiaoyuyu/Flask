from flask import render_template, url_for, session, redirect
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email
# from .. import


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        # 如果没有用户
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            # if current_app.config['FLASKY_ADMIN']:
            send_email('*********@qq.com', 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), current_time=datetime.utcnow())
