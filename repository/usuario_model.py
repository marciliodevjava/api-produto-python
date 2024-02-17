from extensao import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, login, senha, **dados):
        self.nome = nome
        self.login = login
        self.senha = senha

    def __repr__(self):
        return '<Name %r>' % self.nome

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

    @classmethod
    def buscar(cls, login):
        try:
            user = db.session.query(cls).filter_by(login=login).first()
            if user:
                return user
        except Exception:
            return None
