from flask_jwt_extended import jwt_required, exceptions as jwt_exceptions
from flask_restful import Resource, reqparse

from enuns.message import MessageProduto, MessageToken
from repository.produto_model import ProdutoModel
from formulario.preco_formulario import PrecoFormulario

class Produto(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_NOME)
        self.__parser.add_argument('descricao', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_DESCRICAO)
        self.__parser.add_argument('valor', type=float, required=True, help=MessageProduto.PRODUTO_PARSER_VALOR)
        self.__parser.add_argument('preco', type=dict, required=True, help=MessageProduto.PRODUTO_PARSER_PRECO)

    @jwt_required()
    def get(self, nome):
        try:
            produto = ProdutoModel.query.filter_by(nome=nome).first()
            if not produto:
                return {'message': MessageProduto.PRODUTO_NAO_ENCONTRADO.format(nome)}, 404
            return {'Produto': produto.json()}, 200
        except jwt_exceptions.NoAuthorizationError as e:
            return {'message': MessageToken.TOKEN_NAO_AUTORIZADO}, 401
        except Exception as e:
            return {'message': MessageProduto.PRODUTO_ERRO_AO_SALVAR}, 500

    @jwt_required()
    def post(self):
        try:
            dados = self.__parser.parse_args()
            produto = ProdutoModel.query.filter_by(nome=dados.get('nome')).first()

            if not produto:
                produto = ProdutoModel(**dados)
                ProdutoModel.salvar(produto)
                return {
                    'message': MessageProduto.PRODUTO_CRIADO_COM_SUCESSO.format(produto.nome),
                    'produto': produto.json()}, 201
            return {
                'message': MessageProduto.PRODUTO_JA_EXISTE.format(dados.get('nome'))
            }, 200
        except jwt_exceptions.NoAuthorizationError as e:
            return {'message': MessageToken.TOKEN_NAO_AUTORIZADO}, 401
        except Exception as e:
            return {'message': MessageProduto.PRODUTO_ERRO_AO_SALVAR}, 500

    @jwt_required()
    def put(self, id):
        try:
            dados = self.__parser.parse_args()

            produto = ProdutoModel.query.filter_by(id=id).first()
            if produto:
                produto = ProdutoModel(**dados)
                produto.id = id
                ProdutoModel.atualizar(dados, produto)
                return {'message': MessageProduto.PRODUTO_ATUALIZADO,
                        'produto': produto.json()}, 200
            else:
                produto = ProdutoModel(**dados)
                ProdutoModel.salvar(produto)
                return {
                    'message': MessageProduto.PRODUTO_CRIADO_COM_SUCESSO.format(produto.nome),
                    'produto': produto.json()}, 201
        except jwt_exceptions.NoAuthorizationError as e:
            return {'message': MessageToken.TOKEN_NAO_AUTORIZADO}, 401
        except Exception as e:
            return {'message': MessageProduto.PRODUTO_ERRO_AO_SALVAR}, 500

    @jwt_required()
    def delete(self, id):
        try:
            produto = ProdutoModel.buscar(id)
            if produto:
                deletou = ProdutoModel.deletar(produto)
                if deletou:
                    return {'message': MessageProduto.PRODUTO_DELETADO_COM_SUCESSO}
                else:
                    return {'message': MessageProduto.PRODUTO_NAO_FOI_DELETADO}, 500
        except jwt_exceptions.NoAuthorizationError as e:
            return {'message': MessageToken.TOKEN_NAO_AUTORIZADO}, 401
        except Exception as e:
            return {'message': MessageProduto.PRODUTO_ERRO_AO_SALVAR}, 500


class ProdutoTest(Resource):

    @jwt_required()
    def get(self):
        try:
            print('entrou aqui')
        except Exception:
            return {'message': 'message'}

    @jwt_required()
    def post(self):
        try:
            print('entrou aqui')
        except Exception:
            return {'message': 'message'}
