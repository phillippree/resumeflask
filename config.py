import os

class Config(object):
    SECRET_KEY = os.environ.get('RESUME_SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass

class Development(Config):
    DEBUG = True

class Production(Config):

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)



config = {
    'development' : Development,
    'production' : Production
}