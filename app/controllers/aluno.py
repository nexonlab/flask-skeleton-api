from ..errors import UsoInvalido, ErroInterno, TipoErro
from ..dao import aluno as aluno_dao
from . import alchemy_encoder
import simplejson


def recuperar_aluno(cpd=None):
    try:

        resultado = aluno_dao.recupera_aluno(cpd)

        resposta = simplejson.dumps([dict(aluno) for aluno in resultado], default=alchemy_encoder, ensure_ascii=False)

        return resposta
    except ErroInterno as e:
        raise e
    except UsoInvalido as e:
        raise e
    except Exception:
        raise ErroInterno(TipoErro.ERRO_INTERNO.name, payload="Ocorreu um erro ao buscar alunos.")
