import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_SSL', 'True') in ['True', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','10563415SA@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','dwckdclvrrkmynsj')
    APP_MAIL_SUBJECT_PREFIX = '[BuyYourStuff]'
    APP_MAIL_SENDER = os.environ.get('APP_MAIL_SENDER','10563415SA@gmail.com')
    APP_ADMIN = os.environ.get('APP_ADMIN') or '10563415SA@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOMAIN = os.environ.get('DOMAIN','http://localhost:2525')
    STRIPE_KEY = os.environ.get('STRIPE_KEY','sk_test_51JFcO9LOIGzLr6ivCrOjnOHoFJuJr9JSwqGD9Q6FZlVRB7ZZc90IyouZe3c8ffHdbdwimqtXQqQ60EfDHGz7NwLo00vVXhgvko')
    FAKE_API = os.environ.get('FAKE_API','https://fakestoreapi.com/products/')



    SSL_REDIRECT = False
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

#Empty string is used as default value to avoid error while debugging 
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','').replace('postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

class HerokuConfig(ProductionConfig):
    SSL_REDIRECT = True if os.environ.get('DYNO') else False

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle reverse proxy server headers
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        SSL_REDIRECT = True if os.environ.get('DYNO') else False



config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku' : HerokuConfig,
    'default': DevelopmentConfig
}