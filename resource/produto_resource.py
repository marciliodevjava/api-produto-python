from flask_restful import Resource, reqparse

from enuns.message import MessageProduto
from repository.produto_model import ProdutoModel


class Produto(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_NOME)
        self.__parser.add_argument('descricao', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_DESCRICAO)
        self.__parser.add_argument('valor', type=float, required=True, help=MessageProduto.PRODUTO_PARSER_VALOR)

    def get(self, nome):
        produto = ProdutoModel.query.filter_by(nome=nome).first()
        if not produto:
            return {'message': MessageProduto.PRODUTO_NAO_ENCONTRADO.format(nome)}, 404
        return {'Produto': produto.json()}, 200

    def post(self):

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

    def put(self, id):
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
        return {
            'message': MessageProduto.PRODUTO_ERRO_AO_SALVAR}, 500

    def delete(self, id):
        produto = ProdutoModel.buscar(id)


