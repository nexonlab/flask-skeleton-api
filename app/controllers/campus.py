import simplejson
from ..errors import ErroInterno, TipoErro
from ..dao import campus as campus_dao
from . import alchemy_encoder


def recuperar_campus():
    """
    Função que recupera os alunos e trata a resposta para o formato JSON e então retorna para a View Function.

    :return: uma lista de objetos contendo informacoes dos campi.
    :exception ErroInterno
    """
    try:
        resultado = campus_dao.recupera_campus()

        # transforma o resultado da consulta em JSON efetuando um dump para JSON utilizando um encoder proprio
        resposta = simplejson.dumps([dict(aluno) for aluno in resultado], default=alchemy_encoder, ensure_ascii=False)

        return resposta

    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Erro ao recuperar campi disponíveis.")
