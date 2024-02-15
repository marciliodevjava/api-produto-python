from flask_restful import Resource, reqparse
from enuns.message import MessageProduto


class Produto(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('nome', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_NOME)
        self.__parser.add_argument('descricao', type=str, required=True, help=MessageProduto.PRODUTO_PARSER_DESCRICAO)
        self.__parser.add_argument('valor', type=float, required=True, help=MessageProduto.PRODUTO_PARSER_VALOR)

    def get(self):
        pass

    def post(self):
        from repository.produto_model import ProdutoModel

        dados = self.__parser.parse_args()
        produto = ProdutoModel.query.filter_by(nome=dados.get('nome')).first()

        if not produto:
            produto = ProdutoModel(**dados)
            ProdutoModel.salvar(produto)
            return {
                'message': MessageProduto.PRODUTO_CRIADO_COM_SUCESSO.format(produto.nome),
                'produto': produto.json()}, 201
        return {
            'message': MessageProduto.PRODUTO_JA_EXISTE
        }

    def put(self):
        pass

    def delete(self):
        pass
