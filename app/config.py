import urllib
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASK_SLOW_DB_QUERY_TIME = 0.2
    JSON_AS_ASCII = False
    SWAGGER = {
        'title': 'Swagger',
        'doc_dir': os.path.join(os.getcwd(), 'app', 'docs')
    }


class DevelopmentConfig(Config):
    params_conn = 'Driver={ODBC Driver 17 for SQL Server};' \
                  'Server=MY_SERVER;' \
                  'Database=MY_DATABASE;' \
                  'APP={{cookiecutter.app_name}};' \
                  'UID=MY_USER;' \
                  'PWD=MY_PASSWORD;'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus(params_conn)
    DEBUG = True


class TesteConfig(Config):
    DEBUG = True
    TESTING = True
    pass


class CeumaConfig(Config):
    DEBUG = False
    pass


class EuroConfig(Config):
    DEBUG = False
    pass


class FamazConfig(Config):
    DEBUG = False
    pass


class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///%steste.db" % os.path.join(os.getcwd(), "instance/")
