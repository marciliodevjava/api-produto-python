from flask import Flask, jsonify
from flask_restful import Api

from config.config import SQLALCHEMY_DATABASE_URI
from extensao import jwt, db
from resource.login_resource import Login, LoginCadastro
from resource.produto_resource import Produto, ProdutoTest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '123'

jwt.init_app(app)
db.init_app(app)

api = Api(app)

# Adicione seus recursos aqui
api.add_resource(Produto, '/produto', endpoint='post')
api.add_resource(Produto, '/produto/<string:nome>', endpoint='get')
api.add_resource(Produto, '/produto/<int:id>', endpoint='put')
api.add_resource(Produto, '/produto/<int:id>', endpoint='delete')
api.add_resource(ProdutoTest, '/produto-test')

api.add_resource(Login, '/login')
api.add_resource(LoginCadastro, '/cadastro')


@jwt.unauthorized_loader
def unauthorized_loader_callback(callback):
    return jsonify({'message': 'Authorization header is missing'}), 401


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
