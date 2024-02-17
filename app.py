from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from config.config import SQLALCHEMY_DATABASE_URI
from repository.produto_model import db
from resource.login_resource import Login, LoginCadastro
from resource.produto_resource import Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '123'
jwt = JWTManager(app)
db.init_app(app)

api = Api(app)

# Endpoint de Produto
api.add_resource(Produto, '/produto', endpoint='post')
api.add_resource(Produto, '/produto/<string:nome>', endpoint='get')
api.add_resource(Produto, '/produto/<int:id>', endpoint='put')
api.add_resource(Produto, '/produto/<int:id>', endpoint='delete')

# Endpoint de Login
api.add_resource(Login, '/login')

# Endpoint de cadastro de login
api.add_resource(LoginCadastro, '/cadastro')

if __name__ == '__main__':
    app.run(debug=False)
