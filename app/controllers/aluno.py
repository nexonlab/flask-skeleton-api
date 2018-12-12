from ..errors import UsoInvalido, ErroInterno, TipoErro
from ..dao import aluno as aluno_dao
from . import alchemy_encoder
import simplejson


def recuperar_aluno(cpd=None):
    """
    Função que recupera os alunos e trata a resposta para o formato JSON e então retorna para a View Function.

    :param cpd: código do aluno.
    :return: um objeto do tipo JSON pronto para ser enviado como resposta pela view function.
    """
    try:

        resultado = aluno_dao.recupera_aluno(cpd)

        # transforma o resultado da consulta em JSON efetuando um dump para JSON utilizando um encoder proprio
        resposta = simplejson.dumps([dict(aluno) for aluno in resultado], default=alchemy_encoder, ensure_ascii=False)

        return resposta

    except ErroInterno as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Ocorreu um erro ao recuperar aluno(s).")
