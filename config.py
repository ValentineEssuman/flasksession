import os
class DefaultConfig(object):
  PROJECT = ""
  PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
  ROOT_DIR = ""

  DEBUG = True
  TESTING = False

 # SECRET_KEY = os.urandom(24)
  #PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

  # SERVER_NAME = ""
  #PREFERRED_URL_SCHEME = ""

  # ====================================================================
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/postgres')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False