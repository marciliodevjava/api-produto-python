import datetime

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{port}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='1234567890',
        servidor='127.0.0.1',
        port='3306',
        database='produto_python'
    )

SECRET_KEY = '123'
TIME_TOKEN = datetime.timedelta(minutes=59)
NM_ID_SESSAO = "nmIdSessao"
NONE = None
