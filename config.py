import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USERNAME}:{DB_PASSWORD}@{os.environ.get('DATABASE_URL')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
