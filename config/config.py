import os

SECRET_KEY = 'senha'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{port}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='1234567890',
        servidor='127.0.0.1',
        port='3306',
        database='produto_python'
    )