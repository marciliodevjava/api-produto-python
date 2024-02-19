from extensao import db


class PrecoModel(db.Model):
    __tablename__ = 'preco'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, preco):
        self.preco = preco

    def json(self):
        return {
            'id': self.id,
            'preco': self.preco
        }

    @classmethod
    def salvar(cls, preco):
        try:
            db.session.add(preco)
            db.session.commit()
            return preco
        except BaseException:
            return None

    @classmethod
    def atualizar(cls, preco):
        try:
            preco_atualizar = cls.buscar(preco['id'])
            if preco_atualizar:
                preco_atualizar.preco = preco['preco']
                db.session.commit()
                return preco_atualizar
            return None
        except BaseException:
            return None

    @classmethod
    def buscar(cls, id):
        try:
            preco = db.session.query(cls).filter_by(id=id).first()
            if preco:
                return preco
            return None
        except BaseException:
            return None

    @classmethod
    def deletar(cls, preco):
        try:
            db.session.delete(preco)
            db.session.commit()
            return True
        except BaseException:
            return False
