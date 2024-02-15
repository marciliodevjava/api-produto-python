from enuns import Enum


class MessageProduto(Enum):
    PRODUTO_JA_EXISTE = 'O produto {} já existe na base de dados.'
    PRODUTO_CRIADO_COM_SUCESSO = 'O {} foi criado com sucesso!'
    PRODUTO_PARSER_VALOR = 'O campo "valor" não foi enviado.'
    PRODUTO_PARSER_DESCRICAO = 'O campo "descricao" não foi enviado.'
    PRODUTO_PARSER_NOME = 'O campo "nome" não foi enviado.'
