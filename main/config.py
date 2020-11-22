import os


BASEDIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY = '9a00e6f67b3b357e1318fda7471a88dd97dedf18e4a2121430f2b1e837bb74f6'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    IMAGE_UPLOADS = os.path.join(BASEDIR, 'uploads')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+BASEDIR+'/app.db'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= 'sqlite:///'+BASEDIR+'/tests.db'
    DEBUG=True