from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

    @classmethod
    def atualizar(cls, dados, produto):
        id = produto.id
        produto = ProdutoModel.query.filter_by(id=id).first()
        if produto:
            produto.id = id
            produto.nome = dados['nome']
            produto.descricao = dados['descricao']
            produto.valor = dados['valor']
            db.session.commit()

    @classmethod
    def buscar(cls, id):
        produto = ProdutoModel.query.filter_by(id=id).first()
        if produto:
            return produto
        else:
            return None

    @classmethod
    def deletar(cls, produto):
        try:
            db.session.delete(produto)
            db.session.commit()
            return True
        except Exception:
            return None
