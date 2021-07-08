import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_SSL', 'True').lower() in ['True', 'on', '1']
    MAIL_USERNAME = os.environ.get('10563415SA@gmail.com')
    MAIL_PASSWORD = os.environ.get('dwckdclvrrkmynsj')
    APP_MAIL_SUBJECT_PREFIX = '[GetYourStuff]'
    APP_MAIL_SENDER = '10563415SA@gmail.com'
    APP_ADMIN = os.environ.get('APP_ADMIN') or 'meghana.mohapatra93@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.mailtrap.io')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '2525'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['True', 'on', '1']
    MAIL_USERNAME = os.environ.get('74aacdb5c3ef26')
    MAIL_PASSWORD = os.environ.get('428978dff56aff')
    APP_MAIL_SUBJECT_PREFIX = '[GetYourStuff]'
    APP_MAIL_SENDER = 'samarthrout@gmail.com'
    APP_ADMIN = os.environ.get('APP_ADMIN') or 'samarthrout@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_DEFAULT_SENDER= 'samarthrout@gmail.com'
    
    
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '74aacdb5c3ef26'
    app.config['MAIL_PASSWORD'] = '428978dff56aff'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    '''

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}