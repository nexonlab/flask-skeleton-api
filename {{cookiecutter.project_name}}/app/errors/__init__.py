from enum import Enum


class ErroInterno(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict([('erro', self.message), ('status_code', self.status_code), ('mensagem', self.payload)])
        return rv


class UsoInvalido(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict([('erro', self.message), ('status_code', self.status_code), ('mensagem', self.payload)])
        return rv


class TipoErro(Enum):
    INSCRICAO_DUPLICADA = 1
    ERRO_INTERNO = 2
    ERRO_JSON = 3
    ERRO_VALIDACAO = 4
