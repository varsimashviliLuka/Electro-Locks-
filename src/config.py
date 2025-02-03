from dotenv import load_dotenv
import os
from datetime import timedelta
from os import path, sep, pardir

# Load environment variables from a custom path
# load_dotenv(dotenv_path='./env')  # Adjust the path as necessary

class Config(object):
    SECRET_KEY = os.getenv('MY_SECRET_KEY', 'default_secret_key')
    BASE_DIR = path.abspath(path.dirname(__file__) + sep + pardir)
    
    RESTX_MASK_SWAGGER = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')
    
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'default_host')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'default_database')
    MYSQL_USER = os.getenv('MYSQL_USER', 'default_user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'default_password')
    # MySQL connection URI
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=12)
    AUTHORIZATION ={
        'JsonWebToken': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }


class TestConfig(Config):

    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@localhost/{Config.MYSQL_DATABASE}'
    