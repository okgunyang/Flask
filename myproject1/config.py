import os

BASE_DIR = os.path.dirname(__file__)
# sqlite3를 이용하여 pybo.db에 데이터 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False