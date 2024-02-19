from enuns import Enum


class MessageProduto(Enum):
    PRODUTO_PARSER_PRECO = 'É necessario enviar o preço do produto'
    PRODUTO_NAO_FOI_DELETADO = 'Ocorreu um erro ao deletar o produto.'
    PRODUTO_DELETADO_COM_SUCESSO = 'Produto deletado com Sucesso.'
    PRODUTO_ERRO_AO_SALVAR = 'Erro ao salvar produto.'
    PRODUTO_ATUALIZADO = 'Produto atualizado com sucesso!'
    PRODUTO_NAO_ENCONTRADO = 'O produto {} não foi encontrado.'
    PRODUTO_JA_EXISTE = 'O produto {} já existe na base de dados.'
    PRODUTO_CRIADO_COM_SUCESSO = 'O {} foi criado com sucesso!'
    PRODUTO_PARSER_VALOR = "O campo 'valor' não foi enviado."
    PRODUTO_PARSER_DESCRICAO = "O campo 'descricao' não foi enviado."
    PRODUTO_PARSER_NOME = "O campo 'nome' não foi enviado."


class MessageLogin(Enum):
    USUARIO_E_SENHA_INCORRETA = 'Usuário e senha inválidos.'
    USUARIO_SENHA_INCORRETA = 'Senha incorreta, tente novamente.'
    USUARIO_LOGADO_COM_SUCESSO = 'Usuário logado com sucesso!'
    OCORREU_UM_ERRO_AO_SALVAR_USUARIO = 'Ocorreu um erro ao salvar o usuário.'
    USUARIO_CRIADO_COM_SUCESSO = 'Usuário criado com sucesso.'
    USUARIO_JA_EXISTE = 'O Usuário {} já existe, utilize outro nome.'
    SENHA_REQUIRIDO = 'O campo "senha" precisa ser enviado.'
    LOGIN_REQUERIDO = 'O campo "login" precisa ser enviado.'


class MessageToken(Enum):
    TOKEN_EXPIRADO = 'Token expirado, renove o seu token e tente novamente'
    TOKEN_NAO_AUTORIZADO = 'Token inválido.'


class MessagePrecoFormulario(Enum):
    PRECO_PRECISA_SER_ENVIADO = 'O preço precisa ser enviado.'
