from app import db

class ProdutoModel(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)

    def __init__(self, nome, descricao, valor, **dados):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    def __repr__(self):
        return '<Name %r>' % self.nome

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': self.valor
        }

    @classmethod
    def salvar(cls, produto):
        db.session.add(produto)
        db.session.commit()
