from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, login, sneha, **dados):
        self.nome = nome
        self.login = login
        self.senha = sneha

    def json(self):
        return {
            'nome': self.nome,
            'login': self.login
        }

    @classmethod
    def salvar(cls, usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as a:
            return False
