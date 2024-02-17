from secrets import compare_digest

from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from enuns.message import MessageLogin
from repository.usuario_model import UsuarioModel


class Login(Resource):
    def __init__(self):
        self.__parcer = reqparse.RequestParser()
        self.__parcer.add_argument('login', type=str, required=True, help=MessageLogin.LOGIN_REQUERIDO)
        self.__parcer.add_argument('senha', type=str, required=True, help=MessageLogin.SENHA_REQUIRIDO)

    def post(self):
        dados = self.__parcer.parse_args()
        user = UsuarioModel.buscar(dados['login'])
        if user:
            if user and compare_digest(user.senha, dados['senha']):
                access_token = create_access_token(identity=user.id)
                return {
                    'message': MessageLogin.USUARIO_LOGADO_COM_SUCESSO,
                    'acces_token': access_token,
                    'nome': user.nome,
                    'login': user.login
                }, 200
            else:
                return {
                    'message': MessageLogin.USUARIO_SENHA_INCORRETA,
                    'login': dados['login']
                }, 500
        return {
            'message': MessageLogin.USUARIO_E_SENHA_INCORRETA
        }, 500


class LoginCadastro(Resource):
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
        usuario = UsuarioModel(**dados)
        try:
            UsuarioModel.salvar(usuario)
            return {
                'message': MessageLogin.USUARIO_CRIADO_COM_SUCESSO,
                'usuario': usuario.json()
            }, 201
        except Exception as a:
            return {
                'message': MessageLogin.OCORREU_UM_ERRO_AO_SALVAR_USUARIO
            }, 500

    def delete(self):
        pass
