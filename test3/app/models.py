from . import db


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