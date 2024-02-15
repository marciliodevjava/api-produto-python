from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config/config.py')

# Inicialize a instância do SQLAlchemy passando a aplicação como parâmetro
db = SQLAlchemy(app)

api = Api(app)

from resource.produto_resource import Produto

api.add_resource(Produto, '/produto', endpoint='produto')

if __name__ == '__main__':
    app.run(debug=False)
