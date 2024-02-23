from extensao import db
from repository.preco_model import PrecoModel


class ProdutoModel(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    preco_id = db.Column(db.Integer, db.ForeignKey('preco.id'))

    def __init__(self, nome, descricao, valor, preco, **dados):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.preco_id = preco['id']

    def __repr__(self):
        return f'<ProdutoModel(nome={self.nome}, descricao={self.descricao}, valor={self.valor}, preco_id={self.preco_id})>'

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'valor': self.valor,
            'preco': ""
        }

    @classmethod
    def salvar(cls, produto):
        try:

            preco = PrecoModel(produto.preco_id['preco'])
            PrecoModel.salvar(preco)
            db.session.add(produto)
            db.session.commit()
            return produto
        except BaseException:
            return None

    @classmethod
    def atualizar(cls, dados, produto):
        try:
            if produto:
                produto.nome = dados.get('nome', produto.nome)
                produto.descricao = dados.get('descricao', produto.descricao)
                produto.valor = dados.get('valor', produto.valor)
                db.session.commit()
                return produto
            return None
        except BaseException:
            return None

    @classmethod
    def buscar(cls, id):
        try:
            return cls.query.get(id)
        except BaseException:
            return None

    @classmethod
    def deletar(cls, produto):
        try:
            db.session.delete(produto)
            db.session.commit()
            return True
        except BaseException:
            return False
