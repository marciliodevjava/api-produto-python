from flask import Flask
from flask_restful import Api

from config.config import SQLALCHEMY_DATABASE_URI
from repository.produto_model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

from resource.produto_resource import Produto

api.add_resource(Produto, '/produto', endpoint='post')
api.add_resource(Produto, '/produto/<string:nome>', endpoint='get')
api.add_resource(Produto, '/produto/<int:id>', endpoint='put')

if __name__ == '__main__':
    app.run(debug=False)
