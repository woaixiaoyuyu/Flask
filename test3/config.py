class Config:
    SECRET_KEY = 'hard to guess string'

    MAIL_SERVER = 'smtp.qq.com'
    MALT_PORT = 465  # 465 or 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '*********@qq.com'
    MAIL_PASSWORD = '******************'
    FLASKY_ADMIN = '*********@qq.com'  # this is the email of admin
    FLASKY_MAIL_SENDER = '*********@qq.com'  # this is sender
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 只是在主题前面加个修饰前缀

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 静态方法 类或实例均可调用
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*********@localhost/flask'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*********@localhost/flask_test'


class ProductionCongfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:*********@localhost/flask'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionCongfig,
    'default': DevelopmentConfig
}
