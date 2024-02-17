from flask_restful import Resource, reqparse
from enuns.message import MessageLogin
from repository.usuario_model import UsuarioModel


class Login(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('nome', type=str, required=False)
        self.__parcer.add_argument('login', type=str, required=True, help=MessageLogin.LOGIN_REQUERIDO)
        self.__parcer.add_argument('senha', type=str, required=True, help=MessageLogin.SENHA_REQUIRIDO)

    def post(self):
        dados = self.__parcer.parse_args()
        login = UsuarioModel.query.filter_by(login=dados['login']).first()
        if login:
            return {
                'message': MessageLogin.USUARIO_JA_EXISTE.format(dados['login']),
                'usuario': dados.get('login')
            }, 500


class LoginCadastro(Resource):
    def post(self):
        pass

    def delete(self):
        pass
