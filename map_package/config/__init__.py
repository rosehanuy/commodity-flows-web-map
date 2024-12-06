import os

class Config(object):
    DOCKER = os.environ.get('DOCKER', False)

    SECRET_KEY = os.environ.get('SECRET_KEY') or '5E6941EF-6C25-45B7-A79B-6BC159C746CQ'

    POSTGRES_HOST = 'postgis_c' if DOCKER else 'localhost'
    POSTGRES_DB = 'faf'
    POSTGRES_USER = 'rosemary'
    POSTGRES_PWD = 'harriet'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PWD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'